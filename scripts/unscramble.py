#!/usr/bin/env python

from csv import reader
from sys import argv
import sys
from itertools import combinations

wmap = {key: value for key, value in reader(open("dictionary"))}
letters = argv[1][0:15]
for r in range(0, len(letters) - 1):
    comb = set(list(combinations(letters, len(letters) - r)))
    for i in comb:
        s = "".join(sorted(i))
        if s in wmap:
            sys.stdout.write("\n".join(wmap[s].split(",")))
