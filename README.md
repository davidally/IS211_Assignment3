# IS211_Assignment3

### Use:
Accepts valid strings linking to CSV files with `--url` flag.

```sh
# From the command line
 python assignment3.py --url http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv
```
This program will download and parse a CSV file. It will return the amount of image hits 
against total requests as well as the most used browser to make requests. 