import pandas as pd
from typing import List, Dict
import logging
from config import DATA_FILE

logger = logging.getLogger(__name__)

class DataLoader:
    def __init__(self):
        self.data = None
        self._load_data()

    def _load_data(self) -> None:
        """Load and validate the feed mills data from CSV."""
        try:
            self.data = pd.read_csv(DATA_FILE)
            self._validate_data()
            logger.info(f"Successfully loaded data from {DATA_FILE}")
        except Exception as e:
            logger.error(f"Error loading data: {str(e)}")
            raise

    def _validate_data(self) -> None:
        """Validate the loaded data has required columns."""
        required_columns = [
            'Feed Mill Name (English)',
            'Feed Mill Name (Chinese )',
            'Company Website',
            'Country'
        ]
        
        missing_columns = [col for col in required_columns if col not in self.data.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")

    def get_companies(self) -> List[Dict]:
        """Get list of companies with their details."""
        return self.data.to_dict('records')

    def get_company_websites(self) -> List[Dict]:
        """Get list of companies that have websites."""
        return self.data[self.data['Company Website'].notna()].to_dict('records')

    def get_company_names(self) -> List[Dict]:
        """Get list of company names in both English and Chinese."""
        return self.data[['Feed Mill Name (English)', 'Feed Mill Name (Chinese )']].to_dict('records') 