#!/usr/bin/env python3
#
#
import json
import collections
import os.path

def events_per_month(data):
    if not os.path.exists(data):
        return

    print("Number of series/revision per month for %s" % data)
    dates = collections.defaultdict(list)
    fd = open(data)
    for line in fd.readlines():
        series = json.loads(line)
        if series['name'] == 'series-new-revision':
            id, rev = series['series'], series['parameters']['revision']
            dates['-'.join(series['event_time'].split('-')[:2])].append((id, rev))

    for date in sorted(dates.keys()):
        print('%s %s' % (date, len(dates[date])))

events_per_month("data/events/oe-core.json")
events_per_month("data/events/oe.json")
events_per_month("data/events/bitbake.json")


