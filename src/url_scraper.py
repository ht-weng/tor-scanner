"""
@author Haotian Weng
@email haotian.weng@anu.edu.au
@create date 2021-06-22
@modify date 2021-06-24
@desc Scrape Onion URLs from ahmia search engine
"""

import requests
from bs4 import BeautifulSoup

URL = "https://ahmia.fi/address/"


def scrape_urls(file_path):
    """Scrape Onion URLs from ahmia search engine

    Args:
        file_path (str, optional): The list of scraped Onion URLs. Defaults to "../data/onion_urls.txt".
    """
    
    print("Scraping Onion addresses on ahmia.fi")
    # Get html from ahmia
    r = requests.get(URL)
    # Parse html
    soup = BeautifulSoup(r.text, "html.parser")
    # Get links from the html and format the links
    urls = [
        a.get("href").replace("/", "").replace(".ly", "").replace("http:", "")
        for a in soup.find_all("a", href=True)
    ]

    # Write Onion URLs to file
    with open(file_path, "wt+") as f:
        for u in urls:
            # Check whether it is an onion URL
            if ".onion" in u:
                f.write(u + "\n")
    print("Scraping Complete")
