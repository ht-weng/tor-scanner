########################################################################
#
# Generic Makefile
#
# Copyright (c) haotian.weng@anu.edu.au
#
# License: Creative Commons Attribution-ShareAlike 4.0 International.
#
########################################################################

APP=tor-scanner
VER=0.0.1
DATE=$(shell date +%Y-%m-%d)

define HELP
$(APP):
	install	Install dependencies.
	clean	Remove data.
	generate	Sequentially generate unique Onion URLs.
	run
		scrape	Scrape Onion URLs from ahmia.fi.
		ping	Ping Onion URLs and write active URLs to a file.
		scan	Scan ports of active Onion URLs.
endef
export HELP

.PHONY: install
install:
	sudo apt install nmap proxychains4
	pip3 install bs4 requests

.PHONY: clean
clean:
	rm data/*

.PHONY: generate
generate:
