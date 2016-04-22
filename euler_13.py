"""
Euler Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

The numbers are here: https://projecteuler.net/problem=13

"""

import re
import urllib2

def euler_13():

  # Extract the 100 numbers from https://projecteuler.net/problem=13
    url = "https://projecteuler.net/problem=13"
    page_text = urllib2.urlopen(url).read()
    lines = re.findall(r'[0-9]{50}', page_text)
    print len(lines)
    print lines
  # add the numbers together
    total = 0
    for line in lines:
      total += int(line)
  # extract the first 10 integers of the total
    total_formatted = str(total)
    return total_formatted[:10]

print euler_13()