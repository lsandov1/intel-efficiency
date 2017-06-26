import json
import collections
import os.path


def events_per_month(data):
    if not os.path.exists(data):
        return

    dates = collections.defaultdict(list)
    fd = open(data)
    for line in fd.readlines():
        series = json.loads(line)
        if series['name'] == 'series-new-revision':
            id, rev = series['series'], series['parameters']['revision']
            dates['-'.join(series['event_time'].split('-')[:2])].append((id, rev))
    return dates
