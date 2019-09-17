#!/bin/bash

mkdir deps
pip install -t ./deps -r requirements.txt
zip -r Archive *
