# Google Course 6, Lab 2
# Process txt files to dict in python

#! /usr/bin/env python3

import os
import requests

p = "/data/feedback/"

direct = os.listdir(p)

list = []

dkeys = ["title", "name", "date", "feedback"]

for cm in direct:
    keycnt = 0
    feed = {}
    with open(p + cm) as c:
        for ln in c:
            val = ln.strip()
            feed[dkeys[keycnt]] = value
            keycnt += 1
    print(feed)
    resp = requests.post("http://<><>/feedback/", json=feed)

print(resp.request.body)
print(resp.status_code)
