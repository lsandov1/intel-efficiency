#!/usr/bin/env python3

import sys
import glob
import os.path
import re
import subprocess

sys.path.insert(0, os.path.join(os.path.abspath(os.path.dirname(__file__)), 'lib'))
import events


prog = re.compile('(?P<files>\d+) files? changed, (?P<insertions>\d+) insertions?\(\+\), (?P<deletions>\d+) deletions?\(-\)')

data = glob.glob('data/events/oe-core.json')
print('date\tfiles changed\tinsertions\tdeletions')
print('----------------------------------')
for d in data:
    dates = events.events_per_month(d)
    for date in sorted(dates.keys()):
        total_files = total_insertions = total_deletions = 0
        for id, rev in dates[date]:
            cmd = 'git pw mbox %s -r %s' % (id,rev)
            output = subprocess.getoutput(cmd)
            match = prog.search(output)
            if match:
                files, insertions, deletions = match.group('files'), match.group('insertions'), match.group('deletions')
                total_files += int(files)
                total_insertions += int(insertions)
                total_deletions += int(deletions)
        print('%s\t%s\t%s\t%s' % (date, total_files, total_insertions, total_deletions))

