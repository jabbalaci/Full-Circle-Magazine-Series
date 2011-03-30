#!/usr/bin/env python

import os
import os.path
import sys

# extract.py

if len(sys.argv) == 1:
    print "Usage: %s series.csv" % sys.argv[0]
    sys.exit()

# else, if a parameter was passed

f1 = open(sys.argv[1], 'r')

for line in f1:
    if line.startswith('#'):
        continue
    # else
    line = line.rstrip('\n')
    (issue, start_page, end_page) = line.split(';')
    command = "pdftk issues/issue%s_en.pdf cat %s-%s output pieces/%s-%s.pdf" % (issue, start_page, end_page, issue, os.path.splitext(sys.argv[1])[0] )
    print command
    os.system(command)

f1.close()
