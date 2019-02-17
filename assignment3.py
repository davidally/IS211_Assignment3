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

    parsed_file = csv.reader(data)

    # Declaring variables
    total_hits = 0
    img_hits = 0
    browsers = {
        'Chrome': 0,
        'Firefox': 0,
        'IE': 0,
        'Safari': 0
    }

    # Checking data strings for browser type and requested file extensions
    for row in parsed_file:
        if re.search(r'\.(jpg|jpeg|gif|png)$', row[0], re.IGNORECASE):
            img_hits += 1
        # Each row is a hit and automatically tallied
        total_hits += 1
        if re.search('Firefox', row[2], re.IGNORECASE):
            browsers['Firefox'] += 1
        elif re.search('MSIE', row[2]):
            browsers['IE'] += 1
        elif re.search('Safari', row[2]) and not re.search('Chrome', row[2]):
            browsers['Safari'] += 1
        elif re.search('Chrome', row[2]):
            browsers['Chrome'] += 1

    img_percent = (float(img_hits) / total_hits) * 100
    top_browser = max(browsers, key=browsers.get)

    print 'Image requests account for {}% of all requests. The most used browser was {}.'.format(
        img_percent, top_browser)


processData()
