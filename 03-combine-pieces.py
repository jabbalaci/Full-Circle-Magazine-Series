#!/usr/bin/env python

import os
import sys

# combine.py

# one parameter is required and that parameter must be a .csv file
if (len(sys.argv) == 1) or (os.path.splitext(sys.argv[1])[1] != '.csv'):
    print "Usage: {prg} series.csv".format(prg=sys.argv[0])
    print "Tip: the passed parameter file must have .csv extension."
    sys.exit()

# else, if a .csv file was passed

topic = os.path.splitext(sys.argv[1])[0]    # ex. gimp.csv => gimp

dest = "{topic}/result".format(topic=topic)
if not os.path.exists(dest):
    print "Error: {dest} doesn't exist.".format(dest=dest)
    print "Tip: did you execute the 2nd script?"
    sys.exit()

# else, if the destination directory is there

command = "pdftk {topic}/*.pdf cat output {topic}/result/all.pdf".format(topic=topic)
print command
os.system(command)
