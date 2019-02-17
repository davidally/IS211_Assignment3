#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import csv
import urllib2
import argparse
from datetime import datetime

MY_URL = 'http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv'


def downloadData(url):

    response = urllib2.urlopen(url)
    return response


def processData(data=downloadData(MY_URL)):

    # Setting variables
    parsed_file = csv.reader(data)
    total_hits = 0
    img_hits = 0
    # Identifies image file extensions at the end of a string
    img_ext_pattern = r'\.(jpg|jpeg|gif|png)$'

    for row in parsed_file:
        if re.search(img_ext_pattern, row[0], re.IGNORECASE):
            img_hits += 1
        # Each row is a hit and automatically tallied
        total_hits += 1

    img_percent = (float(img_hits) / float(total_hits)) * 100

    print total_hits
    print img_hits

    print 'Image requests account for {}% of all requests.'.format(
        img_percent)


processData()
