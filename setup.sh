#!/bin/bash

# Update package list
yes | pkg update

# Install core dependencies
yes | pkg install python git curl nmap dnsutils

# Install pip and required Python packages
pip install --upgrade pip
pip install requests beautifulsoup4