import sys
import json
import os
import re

link = sys.argv[1]
content = sys.stdin.read()

with open('/home/vagrant/bigdata/scripts/data/html_tags.txt') as f:
    tags = f.read().splitlines()

res = {"link": link}

m_year = re.search("FILE ARCHIVED ON .+, ([1-3][0-9]{3})", content)
if m_year is None:
    res["year"] = 0
else:
    res["year"] = m_year.group(1)

res["webpageLink"] = link[43:(len(link))]

m_inside_begin = re.search("End Wayback Rewrite JS Include -->", content)
m_inside_end = re.search("\s+FILE ARCHIVED ON .+, ", content)
if m_inside_begin is None or m_inside_end is None:
    inside = content
else:
    inside_begin = m_inside_begin.end(0)
    inside_end = m_inside_end.start(0)
    inside = content[inside_begin:(inside_end - 4)]

res["length"] = len(inside)

for tag in tags:
    res[tag] = inside.count(tag)


json_dump = json.dumps({"raw": {"link": link, "content": content}, "parsed": res})
print(json_dump)


