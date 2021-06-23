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
	clean	Remove messy files.
endef
export HELP

help::
	@echo "$$HELP"

.PHONY: install
install:
	sudo apt install nmap proxychains4
	pip3 install bs4 requests
	mkdir data

.PHONY: clean
clean:
	rm -rf src/__pycache__
