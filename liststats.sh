#!/usr/bin/env bash
#
# Computes the number of series per month on OE projects tracked by patchwork
#
#


function stats() {
    project=$1
    data=$2
    echo "Number of series per month (since patchwork launch) in the $project project"

    #2016
    awk '/2016-06/ { count +=1 } END { print "2016-06", count } '  $data
    awk '/2016-07/ { count +=1 } END { print "2016-07", count } '  $data
    awk '/2016-08/ { count +=1 } END { print "2016-08", count } '  $data
    awk '/2016-09/ { count +=1 } END { print "2016-09", count } '  $data
    awk '/2016-10/ { count +=1 } END { print "2016-10", count } '  $data
    awk '/2016-11/ { count +=1 } END { print "2016-11", count } '  $data
    awk '/2016-12/ { count +=1 } END { print "2016-12", count } '  $data


    #2017
    awk '/2017-01/ { count +=1 } END { print "2017-01", count } '  $data
    awk '/2017-02/ { count +=1 } END { print "2017-02", count } '  $data
    awk '/2017-03/ { count +=1 } END { print "2017-03", count } '  $data
    awk '/2017-04/ { count +=1 } END { print "2017-04", count } '  $data
    awk '/2017-05/ { count +=1 } END { print "2017-05", count } '  $data
    awk '/2017-06/ { count +=1 } END { print "2017-06", count } '  $data
 
}

stats "OE-Core" data/oe-core-all-series.txt
stats "Bitbake" data/bitbake-all-series.txt
stats "OE" data/oe-all-series.txt
