#!/Users/jphenri/anaconda3/bin/python3

# Copyright (c) John Henri, All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright notice

"""=========================
simplePlot

The idea behind simplePlot is to create simple tool that will graph a set of numbers
that came out of some benchmark data of something that runs periodically.  If it
succeeded, the benchmark would write the time (in seconds) in a unique text file.
simplePlot reads in those files and creates a line chart in time ascending order.
=========================
"""

# Good spot for matplotlib: https://matplotlib.org/examples/
import matplotlib.pyplot as plt
import sys
import glob
import argparse
import os
from argparse import RawTextHelpFormatter

# Defaults and globals
defaultOutput='data.png'
defaultDir='./'
defaultLabel=''

parser = argparse.ArgumentParser(description=__doc__, formatter_class=RawTextHelpFormatter)
parser.add_argument('-o', '--output', help=('Output image file. Default is %s.' % defaultOutput), default=defaultOutput)
parser.add_argument('-d', '--directory', help=('Directory where data files live.  Default is %s' % defaultDir), default=defaultDir)
parser.add_argument('-l', '--label', help='Add a label to the chart.', default=defaultLabel)
parser.add_argument('pattern', help='Pattern (not regexp) to restrict file candidates to.')
args = parser.parse_args()

pattern = os.path.join(args.directory, args.pattern)
rawFiles = glob.glob(pattern)

# Sort files by date created
files=sorted(rawFiles, key=lambda v: os.path.getctime(v))

# Values that will eventually go into the chart
vals=[]

# This doesn't do any error checking, just assumes one number per file.
# If you need error checking, add some. :)
for dfile in files:
    with open(dfile) as f:
        vals.append(int(f.read()))

fig, ax = plt.subplots()

# Given that we could have a lot of values, just create indexed values for the x axis starting at 1
xValues = list(range(1, len(vals)+1))
line1, = ax.plot(xValues, vals, linewidth=2, marker='x', label=args.label)

ax.legend(loc='lower right')

fig.savefig(args.output)
plt.close(fig)

# TODO, make a lambda variant where the user can pass in a script that can be run on each file to determine the value to chart.
# In other words, this script assumes the file contains a number, but assume it is a longer log file.  Then you'd need a script
# to extract the number we want to chart.  That script would be the lambda script.
