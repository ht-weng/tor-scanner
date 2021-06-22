# Tor Scanner

Tor Scanner is a tool that explores the Tor universe by scanning ports of Tor hidden services.

It sequentially generates unique v2 or v3 Onion URLs and scans those addresses in order.

Tested on Ubuntu 20.04.2.

## Getting started

### Install dependencies

python3-nmap

[proxychains](https://github.com/haad/proxychains)

Install the dependencies using `make`.

```sh
cd tor-scanner/
make depend
```

### Run the scanner

```sh
cd tor-scanner/
python3 main.py 
```

The output files are in the `tor-scanner/data/` folder.
