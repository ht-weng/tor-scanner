# Tor Scanner

Tor Scanner is a tool for exploring the Tor universe by scanning ports of Tor hidden services.

It can sequentially generate unique v2 or v3 Onion URLs and scans those addresses in order.

Tested on Ubuntu 20.04.2.

## Getting started

### Install dependencies

The main dependencies are [nmap](https://nmap.org/) and [proxychains](https://github.com/haad/proxychains).

Install the dependencies using `make`.

```sh
cd tor-scanner/
make install
```

### Adjust proxychains configuration

Adjust timeout values in `/etc/proxychains4.conf`.

### Run the scanner

```sh
cd tor-scanner/
python3 main.py [arguments]
```

Run `python3 main.py -h` to display the help info.

The output files are in the `tor-scanner/data/` folder.

### Clean the mess

```sh
cd tor-scanner/
make clean
```
