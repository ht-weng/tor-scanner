"""
@author Haotian Weng
@email haotian.weng@anu.edu.au
@create date 2021-06-24
@modify date 2021-06-24
@desc Parse arguments and run functions
"""

import argparse
from src import url_generator, url_scraper, scanner


def main():
    parser = argparse.ArgumentParser(description="Tor Scanner - Scan the Onion hidden services")
    parser.add_argument("-g", "--generate", type=int, choices=[2, 3], help="Sequentially generate unique v2 or v3 Onion URLs. Select 2 or 3 to generate v2 or v3 Onion URLs, respectively.")
    parser.add_argument("-S", "--scrape", action="store_true", help="Scrape Onion URLs from ahmia search engine.")
    parser.add_argument("-p", "--ping", action="store_true", help="Ping Onion URLs and write active URLs to a file.")
    parser.add_argument("-s", "--scan", action="store_true", help="Scan ports of Onion URLs and write results to a file.")
    args = parser.parse_args()

    if args.generate:
        if args.generate == 2:
            url_generator.generate_urls(2, "data/onion_urls.txt")
        elif args.generate == 3:
            url_generator.generate_urls(3, "data/onion_urls.txt")
        else:
            raise ValueError("Invalid version number!")
    elif args.scrape:
        url_scraper.scrape_urls("data/onion_urls.txt")
    elif args.ping:
        scanner.ping_onions("data/onion_urls.txt", "data/active_onion_urls.txt")
    elif args.scan:
        scanner.scan_ports("data/active_onion_urls.txt", "data/onions_ports.csv")
    else:
        raise Exception("Please supply an argument!")

if __name__ == "__main__":
    main()