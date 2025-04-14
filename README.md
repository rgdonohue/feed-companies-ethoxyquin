# Feed Companies and Ethoxyquin Research Tool

This tool automates the research of potential links between feed companies and ethoxyquin, producing searchable results for human researchers.

## Setup

1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory with your API keys:
   ```
   GOOGLE_API_KEY=your_api_key
   GOOGLE_CSE_ID=your_custom_search_engine_id
   ```

## Project Structure

```
.
├── data/               # Data files
│   └── feed-mills.csv  # Input data
├── src/               # Source code
│   ├── data_loader.py
│   ├── website_scraper.py
│   ├── web_search.py
│   └── results_processor.py
├── docs/              # Documentation
├── requirements.txt   # Dependencies
└── README.md         # This file
```

## Usage

1. Ensure your data file is in the `data/` directory
2. Run the main script:
   ```bash
   python src/main.py
   ```
3. Results will be saved in the `results/` directory

## Configuration

- Edit `config.py` to modify search parameters
- Adjust rate limiting and delays in the respective modules
- Modify output format in `results_processor.py`

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 