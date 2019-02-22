#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import re
import csv
import urllib2
import argparse
from datetime import datetime


def downloadData(url):
    """This function takes in a URL linking
    to a CSV file and downloads its data. 

    Args:
        url (string): A valid link to a CSV file.

    Returns:
        object: A file like object containing rows of data. 
    """

    response = urllib2.urlopen(url)
    return response


def processData(data):
    """This takes in data from downloadData and
    processes it. It will loop through the data
    checking for specific image file extensions as
    well as most popular browser usage. It will then
    print out an informative string. 

    Args:
        data (object): A file like object containing rows of data.
    """

    # Storing the data in an iterable format
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


def main():
    """This will parse the URL argument in order to download
    CSV data. It will be passed to downloadData and further down
    to processData for searching.

    Raises:
        SystemExit: Exits the program if an error is raised.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument('--url', action='store', type=str,
                        help='Enter a valid link to a CSV file.')
    args = parser.parse_args()

    try:
        data_to_parse = downloadData(args.url)
    except Exception:
        print 'Something went wrong... try entering a valid URL.'
        raise SystemExit
    else:
        processData(data_to_parse)


if __name__ == '__main__':
    main()
