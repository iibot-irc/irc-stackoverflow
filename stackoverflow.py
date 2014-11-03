#!/usr/bin/env python

import feedparser, sys


tag = sys.argv[1]
STATEFILE = sys.argv[2]

url="http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % tag
d = feedparser.parse(url)

sf = open(STATEFILE)
seen = set(sf.read().split("\n"))
sf.close()

new=[]
for question in d['entries']:
  if not question['id'] in seen:
    new.append(question['id'])
    print question['title']+":", question["link"], "by", question["author"]

if len(new) != 0:
  f = open(STATEFILE, "a")
  for new in new:
    f.write(new+"\n")
  f.close()
