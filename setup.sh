#!/bin/bash

#==================================================#
# Setup the python environment
#==================================================#
echo "Setting up Python Tools"
sudo apt-get install python-setuptools
sudo easy_install virtualenv
sudo easy_install pip

#==================================================#
# Setup Virtual Environment
#==================================================#
echo "Setting up Virtual Environment"
virtualenv .venv
source .venv/bin/activate
easy_install pip
pip install django
