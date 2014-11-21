#!/usr/bin/env python
import feedparser, sys

tag = sys.argv[1]
STATEFILE = sys.argv[2]

url="http://stackoverflow.com/feeds/tag?tagnames=%s&sort=newest" % tag
d = feedparser.parse(url)

with open(STATEFILE) as sf:
  seen = set(sf.read().split("\n"))

for question in d['entries']:
  if not question['id'] in seen:
    with open(STATEFILE, "a") as f:
      f.write(new+"\n")
    new.append(question['id'])
    print question['title']+":", question["link"], "by", question["author"]
