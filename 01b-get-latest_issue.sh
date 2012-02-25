#!/usr/bin/env bash

# get the latest issue only

wget -c `tail -1 issues.txt` -P issues/ 
