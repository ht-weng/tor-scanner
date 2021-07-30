"""
@author Haotian Weng
@email haotian.weng@anu.edu.au
@create date 2021-06-22
@modify date 2021-06-24
@desc Ping and scan ports of unique Onion URLs
"""

import subprocess
import re

# See https://nmap.org/book/man-port-scanning-basics.html for references
# PORTS = [
#     "20",
#     "21",
#     "22",
#     "23",
#     "25",
#     "26",
#     "53",
#     "80",
#     "81",
#     "110",
#     "113",
#     "135",
#     "161",
#     "143",
#     "443",
#     "445",
#     "587",
#     "993",
#     "995",
#     "1337",
#     "1433",
#     "2525",
#     "3306",
#     "4444",
#     "5222",
#     "5223",
#     "5901",
#     "6667",
#     "6668",
#     "6669",
#     "6697",
#     "8060",
#     "8080",
#     "8081",
#     "8333",
#     "9051",
#     "9200",
#     "9500",
#     "9878",
#     "10000",
#     "11009",
#     "15441",
#     "17993",
#     "22222",
#     "27017",
#     "31337",
# ]


PORTS = [
    "21",
    "22",
    "23",
    "25",
    "80",
    "110",
    "143",
    "443",
    "3306",
    "8080",
]


def ping_onions(urls_file, results_file):
    """Ping Onion URLs and write active URLs to a file

    Args:
        urls_file (str, optional): The list of Onion ULRs to ping. Defaults to "../data/onion_urls.txt".
        results_file (str, optional): The list of active Onion URLs. Defaults to "../data/active_onion_urls.txt".
    """
    with open(urls_file, "r") as url_list, open(results_file, "w+") as results_list:

        for url in url_list:
            url = url.replace("\n", "")

            # Use proxychains as the Tor proxy
            # Scan port 80 with nmap
            # Since port 80 is the common port, use it as the indicator of the status
            print("Ping ", url)
            ping_result = subprocess.Popen(
                ["proxychains4", "-q", "nmap", "-oG", "-", "-p", "80", url],
                stdout=subprocess.PIPE,
            )
            ping_text, _ = ping_result.communicate()
            # Get the status from the command output using regular expression
            status_80 = re.search("80/(.*?)/", str(ping_text)).group(1)
            if status_80 != "closed":
                # Write active URLs to the file
                status = "Up"
                results_list.write(url)
                results_list.write("\n")
            else:
                status = "Down"
            print("Status of ", url, " : ", status)


def scan_ports(urls_file, results_file):
    """Scan ports of Onion URLs and write results to a file

    Args:
        urls_file (str, optional): The list of active Onion URLs to scan. Defaults to "../data/active_onion_urls.txt".
        results_file (str, optional): Onion URLs and the status of ports. Defaults to "../data/onions_ports.csv".
    """
    with open(urls_file, "r") as url_list, open(results_file, "w+") as results_csv:
        # Write headers
        results_csv.write(",".join(["url"] + PORTS))
        results_csv.write("\n")

        for url in url_list:
            url = url.replace("\n", "")
            print("Scanning ", url)
            # Use proxychains as the Tor proxy
            # Scan the ports with nmap
            scan_result = subprocess.Popen(
                ["proxychains4", "-q", "nmap", "-oG", "-", "-p", ",".join(PORTS), url],
                stdout=subprocess.PIPE,
            )
            scan_text, _ = scan_result.communicate()
            port_status = []
            for port in PORTS:
                # Get the status of ports from the command output using regular expression
                status = re.search(port + "/(.*?)/", str(scan_text)).group(1)
                port_status.append(status)
            ports_and_status = zip(PORTS, port_status)
            print("Ports of ", url, ": ", tuple(ports_and_status))
            # Write ports' status to the file
            line_to_write = [url] + port_status
            results_csv.write(",".join(line_to_write))
            results_csv.write("\n")
