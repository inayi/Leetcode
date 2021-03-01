#!/usr/bin/env python3

# 1360. Write a program to count the number of days between two dates.
# The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

from datetime import datetime

# input format is YYYY-MM-DD
date1 = "2020-01-15"
date2 = "2019-12-31"

d1 = datetime.strptime(date1, '%Y-%m-%d')
d2 = datetime.strptime(date2, '%Y-%m-%d')

# good use of abs
print(abs((d2 - d1).days))
