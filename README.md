# SmartPrix Smartphone Data Insights

[![Python](https://img.shields.io/badge/python-3.10-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

---

## Project Overview

**SmartPrix Smartphone Data Insights** is a Python project designed to **collect, clean, and analyze smartphone data** from the [SmartPrix](https://www.smartprix.com/) website. This project demonstrates a complete data pipeline from web scraping to visualization, providing actionable insights on:

- Smartphone pricing trends
- Brand-wise comparisons
- Feature analysis (RAM, storage, camera, etc.)
- Market segmentation (budget, mid-range, premium)

The workflow follows this sequence:

1. Web scraping using Selenium for dynamic content  
2. Web scraping using BeautifulSoup for static content  
3. Data cleaning and preprocessing  
4. Exploratory Data Analysis (EDA) and visualization  

---

## Project Goals

- Build a robust **data pipeline** for smartphone data collection.  
- Demonstrate **data cleaning and preprocessing** best practices.  
- Provide **visual insights** for smartphones using Python visualization libraries.  
- Enable future **machine learning or recommendation system** applications.  

---

## Folder Structure

```
smartprix-smartphone-data-insights/
│
├── src/
│   ├── 01_selenium_scraping.py       # Selenium scraping
│   ├── 02_beautiful_soup_scraping.py # BeautifulSoup scraping (uses smartprix.html)
│   ├── 03_cleaning.py                # Data cleaning
│   └── 04_eda.py           # EDA & plotting
│
├── notebooks/
│   ├── 01_selenium_scraping.ipynb
│   └── 02_beautiful_soup_scraping.ipynb
│
├── data/
│   ├── html/
│   │   └── smartprix.html            # Intermediate HTML used by BeautifulSoup script
│   ├── raw/                          # Local raw dataset (not pushed to GitHub)
│   │   └── phones_data.xlsx
│   └── cleaned/                      # Local cleaned dataset (not pushed to GitHub)
│       └── cleaned__smartphone_data.xlsx
│
├── plots/
│   └── *.png                         # Saved EDA visualizations
│
├── .gitignore
├── requirements.txt
└── README.md
```

> Note: Large Excel datasets in `data/raw` and `data/cleaned` are ignored in `.gitignore` to keep the repo size manageable. Users need to provide their own datasets in the same structure.

---

## Prerequisites

- Python 3.x  
- Pip package manager  
- Web driver for Selenium (e.g., ChromeDriver)  

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Web Scraping

```bash
# Selenium scraping (dynamic content)
python src/01_selenium_scraping.py

# BeautifulSoup scraping (static content)
python src/02_beautiful_soup_scraping.py
```

> The BeautifulSoup script generates and/or uses `data/html/smartprix.html` as intermediate HTML for further processing.

### 2. Data Cleaning

```bash
python src/03_cleaning.py
```

* Cleans and preprocesses raw scraped data
* Produces `data/cleaned/cleaned__smartphone_data.xlsx`

### 3. Exploratory Data Analysis (EDA)

```bash
python src/04_visualization.py
```

* Generates visualizations from the cleaned dataset
* Saves plots as PNG files in `plots/`

---

## Datasets

* **Raw data:** `data/raw/phones_data.xlsx` (user-provided or generated via scraping)
* **Cleaned data:** `data/cleaned/cleaned__smartphone_data.xlsx` (produced by `03_cleaning.py`)
* **Intermediate HTML:** `data/html/smartprix.html` (used by `02_beautiful_soup_scraping.py`)

> Users must provide raw Excel datasets in `data/raw/` to run the full pipeline.

---

## Example Outputs

* **Price Distribution:** Histogram showing smartphone prices across all brands
* **Brand Comparison:** Bar chart comparing average prices of top smartphone brands
* **Feature Analysis:** Scatter plots showing RAM, storage, and camera trends
* **Market Segmentation:** Pie chart of budget, mid-range, and premium phones

---

## Dependencies

* `selenium`
* `beautifulsoup4`
* `pandas`
* `matplotlib`
* `seaborn`
* `openpyxl`
* `jupyter` (optional for notebooks)

```bash
pip install -r requirements.txt
```

---

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/your-feature`)
3. Make your changes
4. Commit your changes (`git commit -m "Add your message"`)
5. Push to the branch (`git push origin feature/your-feature`)
6. Open a Pull Request

---

## License

This project is licensed under the **MIT License**.
