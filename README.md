# CountryRiskProfiler

This project is designed to scrape country compliance and risk data from the [Know Your Country](https://www.knowyourcountry.com/country-reports/) website and process the data into a structured format for further analysis. The data is then converted into a CSV file, which can be used for reporting or integrated into other systems.

## Table of Contents

- [Overview](#overview)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [License](#license)
- [Contributing](#contributing)

## Overview

The project is composed of two main scripts:

1. **run1.py**: This script uses Selenium to automate the extraction of country risk data from the Know Your Country website. It scrapes each country's name, risk rating, and detailed compliance metrics (color-coded) and saves this information into a JSON file.

2. **run2.py**: This script processes the JSON file generated by `run1.py`, mapping the color-coded compliance metrics to numerical values, and then saves the structured data into a CSV file for further analysis.

## Project Structure

```plaintext
.
├── LICENSE
├── README.md
├── country_data.csv       # Generated CSV file containing the processed data
├── country_data.json      # JSON file containing raw scraped data
├── requirements.txt       # Python dependencies for the project
├── src
│   ├── run1.py            # Selenium-based scraper script
│   └── run2.py            # Data processing script
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your_username/country-risk-analysis-scraper.git
   cd country-risk-analysis-scraper
   ```

2. **Install the required dependencies:**

   Make sure you have Python 3.x installed. Then, install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` includes necessary libraries such as `selenium`, `webdriver-manager`, and `pandas`.

3. **Set up WebDriver:**

   The project uses `webdriver-manager` to automatically manage the Chrome WebDriver, so no additional setup is needed.

## Usage

### Running the Scraper (run1.py)

This script navigates to the Know Your Country website and scrapes data for each country, saving it into a JSON file.

```bash
python src/run1.py
```

The script will automatically scroll through the country list, extract the relevant data, and save it in `country_data.json`.

### Processing the Data (run2.py)

Once the scraping is complete, you can process the JSON file to convert the data into a structured CSV format:

```bash
python src/run2.py
```

This script will read `country_data.json`, map the color-coded compliance data to numerical values, and save the processed data in `country_data.csv`.

## Output

- **country_data.json**: This file contains the raw scraped data, with each country's name, risk rating, and a list of compliance details (color-coded).
- **country_data.csv**: The processed CSV file, where each country is a row, and columns represent the country name, risk rating, and the numerical values of compliance details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, please open an issue or submit a pull request.

