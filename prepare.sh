#!/bin/bash

mkdir dependencies
pip install -t ./dependencies -r requirements.txt
rm Archive.zip
zip -r Archive *
