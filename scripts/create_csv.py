#!/usr/bin/env python

wlist = (open("words", "r").read()).rsplit()
d = {}

for word in wlist:
    s = "".join(sorted(word))
    if s not in d:
        d[s] = word
    else:
        d[s] += "," + word
for key, value in sorted(d.items()):
    print(key.lower() + "," + '"' + value.lower() + '"')
