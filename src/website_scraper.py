import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from typing import List, Dict, Optional
import time
import logging
import urllib.parse
from config import USER_AGENT, REQUEST_DELAY, MAX_RETRIES, TIMEOUT, KEYWORDS

logger = logging.getLogger(__name__)

class WebsiteScraper:
    def __init__(self):
        self.headers = {'User-Agent': USER_AGENT}
        self.driver = None

    def __del__(self):
        if self.driver:
            self.driver.quit()

    def _validate_url(self, url: str) -> bool:
        """Validate if the URL is properly formatted."""
        if not url or url.strip() == '-':
            return False
            
        try:
            result = urllib.parse.urlparse(url)
            return all([result.scheme, result.netloc])
        except Exception:
            return False

    def _setup_selenium(self) -> None:
        """Set up Selenium WebDriver for JavaScript-rendered content."""
        if not self.driver:
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            options.add_argument(f'user-agent={USER_AGENT}')
            options.add_argument('--ignore-certificate-errors')  # Ignore SSL errors
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=options)

    def search_website(self, url: str) -> List[Dict]:
        """Search a website for keywords and return matches."""
        results = []
        
        if not self._validate_url(url):
            logger.warning(f"Invalid URL: {url}")
            return results
            
        try:
            # First try with requests
            content = self._get_content_requests(url)
            if content:
                matches = self._find_keywords(content)
                if matches:
                    results.extend(matches)
            
            # If no matches found, try with Selenium
            if not results:
                content = self._get_content_selenium(url)
                if content:
                    matches = self._find_keywords(content)
                    if matches:
                        results.extend(matches)

        except Exception as e:
            logger.error(f"Error searching website {url}: {str(e)}")

        return results

    def _get_content_requests(self, url: str) -> Optional[str]:
        """Get website content using requests."""
        for attempt in range(MAX_RETRIES):
            try:
                # Try with SSL verification first
                response = requests.get(url, headers=self.headers, timeout=TIMEOUT, verify=True)
                response.raise_for_status()
                return response.text
            except requests.exceptions.SSLError:
                # If SSL verification fails, try without verification
                try:
                    response = requests.get(url, headers=self.headers, timeout=TIMEOUT, verify=False)
                    response.raise_for_status()
                    return response.text
                except Exception as e:
                    logger.warning(f"Attempt {attempt + 1} failed for {url} (SSL bypass): {str(e)}")
            except Exception as e:
                logger.warning(f"Attempt {attempt + 1} failed for {url}: {str(e)}")
            time.sleep(REQUEST_DELAY)
        return None

    def _get_content_selenium(self, url: str) -> Optional[str]:
        """Get website content using Selenium."""
        try:
            self._setup_selenium()
            self.driver.get(url)
            time.sleep(REQUEST_DELAY)  # Wait for JavaScript to load
            return self.driver.page_source
        except Exception as e:
            logger.error(f"Selenium error for {url}: {str(e)}")
            return None

    def _find_keywords(self, content: str) -> List[Dict]:
        """Find keywords in the content and return matches with context."""
        matches = []
        soup = BeautifulSoup(content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)

        for keyword in KEYWORDS:
            if keyword in text:
                # Find the context around the keyword
                start = max(0, text.find(keyword) - 100)
                end = min(len(text), text.find(keyword) + 100)
                context = text[start:end]
                
                matches.append({
                    'keyword': keyword,
                    'context': context
                })

        return matches 