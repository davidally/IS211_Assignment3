# IS211_Assignment3

### Use:
Pass a valid URL linking to a CSV file into the `url` parameter.
```sh
# From the command line
 python assignment3.py http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
```
This program will download and parse a CSV file. It will return the amount of image hits 
against total requests as well as the most used browser to make requests. 