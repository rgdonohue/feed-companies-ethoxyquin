import requests
from typing import List, Dict
import time
import logging
from config import GOOGLE_API_KEY, GOOGLE_CSE_ID, REQUEST_DELAY, KEYWORDS

logger = logging.getLogger(__name__)

class WebSearch:
    def __init__(self):
        if not GOOGLE_API_KEY or not GOOGLE_CSE_ID:
            raise ValueError("Google API key and CSE ID must be set in environment variables")

    def search_company(self, company_name: str, company_name_chinese: str) -> List[Dict]:
        """Search for company name combined with each keyword."""
        results = []
        
        # Create search queries combining company name with each keyword
        queries = []
        for keyword in KEYWORDS:
            queries.append(f"{company_name} {keyword}")
            queries.append(f"{company_name_chinese} {keyword}")

        # Execute searches
        for query in queries:
            try:
                search_results = self._execute_search(query)
                if search_results:
                    results.extend(search_results)
                time.sleep(REQUEST_DELAY)  # Respect rate limits
            except Exception as e:
                logger.error(f"Error searching for query '{query}': {str(e)}")

        return results

    def _execute_search(self, query: str) -> List[Dict]:
        """Execute a single search using Google Custom Search API."""
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': GOOGLE_API_KEY,
            'cx': GOOGLE_CSE_ID,
            'q': query,
            'num': 10  # Number of results to return
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            data = response.json()

            results = []
            if 'items' in data:
                for item in data['items']:
                    results.append({
                        'title': item.get('title', ''),
                        'snippet': item.get('snippet', ''),
                        'link': item.get('link', ''),
                        'query': query
                    })

            return results
        except Exception as e:
            logger.error(f"API error for query '{query}': {str(e)}")
            return [] 