#!/usr/bin/env bash

# get ALL issues

wget -c -i issues.txt -P issues/ 
mv issues/fullcircle-issue28-eng1.pdf issues/issue28_en.pdf 2>/dev/null
