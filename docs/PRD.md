# Product Requirements Document: Feed Companies and Ethoxyquin Research Tool

## 1. Project Overview
**Objective**: Create an automated tool to research potential links between feed companies and ethoxyquin, producing searchable results for human researchers.

## 2. Core Requirements

### 2.1 Data Input
- Source data from provided CSV file (`feed-mills.csv`)
- Required fields per company:
  - English name
  - Chinese name
  - Website URL (if available)
  - Country
  - Ownership information

### 2.2 Search Keywords
- Primary chemical terms:
  - English: "Ethoxyquin"
  - Chinese variations:
    - 乙氧喹啉
    - 乙氧基喹啉
    - 1,2-二氢-6-乙氧基-2,2,4-三甲基喹
    - 山道喹
    - 虎皮灵
  - Tariff code: 2933490013

### 2.3 Search Methods

#### 2.3.1 Website Scraping
- For companies with websites:
  - Implement respectful web scraping with proper headers and delays
  - Handle both English and Chinese content
  - Support JavaScript-rendered content (using Selenium if needed)
  - Implement error handling and rate limiting

#### 2.3.2 Web Search
- Implement search using:
  - Company name (English)
  - Company name (Chinese)
  - Combined with each keyword
- Support both English and Chinese search results
- Implement proper API key management

### 2.4 Output Requirements
- Generate structured results in CSV format
- Each result should include:
  - Company name
  - Source (website/web search)
  - Keyword found
  - Context/snippet
  - URL of source
  - Timestamp of search

## 3. Technical Architecture

### 3.1 Core Components
1. **Data Loader**
   - CSV parser
   - Data validation
   - UTF-8 encoding support

2. **Website Scraper**
   - BeautifulSoup for HTML parsing
   - Selenium for JavaScript content
   - Rate limiting and error handling
   - User agent rotation

3. **Web Search Module**
   - Search API integration
   - Query builder
   - Result parser
   - Rate limiting

4. **Results Processor**
   - Data aggregation
   - Duplicate detection
   - CSV export

### 3.2 Dependencies
- Python 3.x
- Required packages:
  - pandas
  - requests
  - beautifulsoup4
  - selenium
  - search API client (e.g., Google Custom Search API)

## 4. Implementation Phases

### Phase 1: Setup and Basic Infrastructure
1. Set up project structure
2. Implement CSV reader
3. Create basic search functions
4. Set up logging and error handling

### Phase 2: Website Scraping
1. Implement basic website scraping
2. Add JavaScript support
3. Implement rate limiting
4. Test with sample websites

### Phase 3: Web Search Integration
1. Set up search API
2. Implement query building
3. Add result parsing
4. Test search functionality

### Phase 4: Results Processing
1. Implement results aggregation
2. Create CSV export
3. Add duplicate detection
4. Test full pipeline

## 5. Security and Compliance

### 5.1 API Key Management
- Store API keys in environment variables
- Never commit API keys to version control
- Document key management process

### 5.2 Web Scraping Compliance
- Respect robots.txt
- Implement proper delays between requests
- Use appropriate user agents
- Handle errors gracefully

## 6. Deliverables

### 6.1 Code
- Well-documented Python scripts
- Configuration files
- Requirements.txt
- README.md with setup instructions

### 6.2 Documentation
- API documentation
- Setup guide
- Usage instructions
- Troubleshooting guide

### 6.3 Results
- CSV file with search results
- Log files
- Summary report

## 7. Success Metrics
- Number of companies successfully processed
- Percentage of websites successfully scraped
- Number of relevant results found
- Processing time per company
- Error rate

## 8. Future Enhancements
- Add support for additional languages
- Implement machine learning for result relevance
- Add automated result categorization
- Support for additional data sources
- Web interface for results visualization 