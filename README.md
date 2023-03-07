# pokedex-scraping
## Description
Python script that scrapes data about the Pokemon from the [Serebii.net](https://serebii.net) website. It collects information about each Pokemon's name, number, image, and stats. The script uses the Python libraries `requests` and `BeautifulSoup` to scrape the data from the website, and `pandas` to store the data in a Pandas dataframe. Google Drive's API `gspread` library is used to upload the following information onto a Google Sheet with the sheet names corresponding to the correct information. 

## Installation
To use the web scraper, need to have Python3 installed on local machine. Python3 can be installed from official [Python website](https://www.python.org/downloads/).
Will also need to install Python libraries, `requests`, `beautifulsoup4`, `pandas`, and `gspread`. The libraries can be installed by running following command in terminal:

`pip install requests beautifulsoup4 pandas gspread`

## Usage
First, create a Google Sheet with the file name you want, and change `sheet_name` variable in upload.py to match the file name. Run upload.py to populate the data onto the Google Sheet file.

## Acknowledgments
Thanks to [Serebii.net](https://serebii.net) website for providing the data used in this project.
