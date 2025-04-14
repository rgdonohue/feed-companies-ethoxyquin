import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Search keywords
KEYWORDS = [
    'Ethoxyquin',
    '乙氧喹啉',
    '乙氧基喹啉',
    '1,2-二氢-6-乙氧基-2,2,4-三甲基喹',
    '2933490013',
    '山道喹',
    '虎皮灵'
]

# API Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID')

# Web Scraping Configuration
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
REQUEST_DELAY = 2  # seconds between requests
MAX_RETRIES = 3
TIMEOUT = 10  # seconds

# File Paths
DATA_FILE = 'data/feed-mills.csv'
RESULTS_DIR = 'results'
LOG_FILE = 'results/search.log'

# Output Configuration
OUTPUT_COLUMNS = [
    'company_name',
    'company_name_chinese',
    'source',
    'keyword_found',
    'context',
    'url',
    'timestamp'
] 