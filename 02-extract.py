#!/usr/bin/env python

import os
import sys
import errno

# extract.py

# one parameter is required and that parameter must be a .csv file
if (len(sys.argv) == 1) or (os.path.splitext(sys.argv[1])[1] != '.csv'):
    print "Usage: {prg} series.csv".format(prg=sys.argv[0])
    print "Tip: the passed parameter file must have .csv extension."
    sys.exit()

# else, if a .csv file was passed

topic = os.path.splitext(sys.argv[1])[0]    # ex. gimp.csv => gimp

try:
    os.makedirs("{topic}/result".format(topic=topic))
except OSError as exc:
    if exc.errno == errno.EEXIST:
        pass
    else: raise

f1 = open(sys.argv[1], 'r')

for line in f1:
    if line.startswith('#'):
        continue
    # else
    line = line.rstrip('\n')
    (issue, start_page, end_page) = line.split(';')
    command = "pdftk issues/issue{n}_en.pdf cat {start}-{end} output {topic}/{issue}-{topic}.pdf".format(n=issue, start=start_page, end=end_page, issue=issue, topic=topic)
    print command
    os.system(command)

f1.close()
