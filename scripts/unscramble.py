#!/usr/bin/env python

from csv import reader
from sys import argv
import sys
from itertools import combinations

wmap = {key: value for key, value in reader(open("dictionary"))}
letters = argv[1][0:20]
for r in range(0, len(letters) - 1):
    comb = set(["".join(sorted(i)) for i in list(combinations(letters, len(letters) - r))])
    for i in comb:
        s = "".join(sorted(i))
        try:
            sys.stdout.write(wmap[s] + "\n")
        except KeyError:
            pass
