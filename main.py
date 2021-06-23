import argparse
import subprocess

from src import url_generator


def main():
    parser = argparse.ArgumentParser(description="Tor Scanner - Scan the Onion hidden services")
    parser.add_argument("-g", "--generate", help="Sequentially generate unique Onion URLs")
    parser.add_argument("-S", "--scrape", help="Scrape Onion URLs from ahmia search engine")
    parser.add_argument("-p", "--ping", help="Ping Onion URLs and write active URLs to a file")
    parser.add_argument("-s", "--scan", help="Scan ports of Onion URLs and write results to a file")
    args = parser.parse_args()

    if args.generate:
        url_generator.generate_urls()
    else:
        print("Please supply an argument!")

if __name__ == "__main__":
    main()