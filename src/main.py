import logging
from data_loader import DataLoader
from website_scraper import WebsiteScraper
from web_search import WebSearch
from results_processor import ResultsProcessor
from config import LOG_FILE

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    try:
        # Initialize components
        logger.info("Initializing components...")
        data_loader = DataLoader()
        website_scraper = WebsiteScraper()
        web_search = WebSearch()
        results_processor = ResultsProcessor()

        # Get companies with websites
        companies_with_websites = data_loader.get_company_websites()
        logger.info(f"Found {len(companies_with_websites)} companies with websites")

        # Search company websites
        logger.info("Searching company websites...")
        for company in companies_with_websites:
            logger.info(f"Searching website for {company['Feed Mill Name (English)']}")
            matches = website_scraper.search_website(company['Company Website'])
            if matches:
                results_processor.add_website_result(company, matches)

        # Get all companies for web search
        companies = data_loader.get_companies()
        logger.info(f"Found {len(companies)} total companies")

        # Perform web searches
        logger.info("Performing web searches...")
        for company in companies:
            logger.info(f"Searching web for {company['Feed Mill Name (English)']}")
            search_results = web_search.search_company(
                company['Feed Mill Name (English)'],
                company['Feed Mill Name (Chinese )']
            )
            if search_results:
                results_processor.add_web_search_result(company, search_results)

        # Export results
        logger.info("Exporting results...")
        results_file = results_processor.export_results()
        
        # Print summary
        summary = results_processor.get_summary()
        logger.info("\nResults Summary:")
        logger.info(f"Total results: {summary['total_results']}")
        logger.info("\nResults by source:")
        for source, count in summary['by_source'].items():
            logger.info(f"  {source}: {count}")
        logger.info("\nResults by keyword:")
        for keyword, count in summary['by_keyword'].items():
            logger.info(f"  {keyword}: {count}")

        logger.info(f"\nResults exported to: {results_file}")

    except Exception as e:
        logger.error(f"Error in main process: {str(e)}")
        raise

if __name__ == "__main__":
    main() 