#!/usr/bin/env python3
#
#

import sys
import glob
import os.path

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))

import events
import glob

data = glob.glob('data/events/*.json')
for d in data:
    print("Number of series/revision per month for %s" % d)
    dates = events.events_per_month(d)
    for date in sorted(dates.keys()):
        print('%s %s' % (date, len(dates[date])))
