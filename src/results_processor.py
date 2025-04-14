import pandas as pd
from typing import List, Dict
import logging
from datetime import datetime
from config import RESULTS_DIR, OUTPUT_COLUMNS, LOG_FILE

logger = logging.getLogger(__name__)

class ResultsProcessor:
    def __init__(self):
        self.results = []
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Set up logging configuration."""
        logging.basicConfig(
            filename=LOG_FILE,
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    def add_website_result(self, company: Dict, matches: List[Dict]) -> None:
        """Add website search results to the collection."""
        for match in matches:
            self.results.append({
                'company_name': company['Feed Mill Name (English)'],
                'company_name_chinese': company['Feed Mill Name (Chinese )'],
                'source': 'website',
                'keyword_found': match['keyword'],
                'context': match['context'],
                'url': company['Company Website'],
                'timestamp': datetime.now().isoformat()
            })

    def add_web_search_result(self, company: Dict, search_results: List[Dict]) -> None:
        """Add web search results to the collection."""
        for result in search_results:
            self.results.append({
                'company_name': company['Feed Mill Name (English)'],
                'company_name_chinese': company['Feed Mill Name (Chinese )'],
                'source': 'web_search',
                'keyword_found': result['query'].split()[-1],  # Extract keyword from query
                'context': result['snippet'],
                'url': result['link'],
                'timestamp': datetime.now().isoformat()
            })

    def export_results(self) -> str:
        """Export results to CSV file."""
        if not self.results:
            logger.warning("No results to export")
            return ""

        # Create DataFrame
        df = pd.DataFrame(self.results)
        
        # Ensure all required columns exist
        for col in OUTPUT_COLUMNS:
            if col not in df.columns:
                df[col] = ''

        # Reorder columns
        df = df[OUTPUT_COLUMNS]

        # Generate filename with timestamp
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        filename = f"{RESULTS_DIR}/results_{timestamp}.csv"

        # Export to CSV
        df.to_csv(filename, index=False, encoding='utf-8')
        logger.info(f"Results exported to {filename}")

        return filename

    def get_summary(self) -> Dict:
        """Generate a summary of the results."""
        if not self.results:
            return {
                'total_results': 0,
                'by_source': {},
                'by_keyword': {}
            }

        df = pd.DataFrame(self.results)
        
        summary = {
            'total_results': len(self.results),
            'by_source': df['source'].value_counts().to_dict(),
            'by_keyword': df['keyword_found'].value_counts().to_dict()
        }

        return summary 