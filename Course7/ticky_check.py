#!/usr/bin/env python3

import re
import csv
import operator

per_user = {}
Error = {}

with open("syslog.log", "r") as lines:
	for line in lines.readlines():
		reg = re.search(r"ticky: ERROR: ([\w ]*) ", line)
		
		if reg is None:
			continue
		
		if reg.group(1) not in Error:
			Error[reg.group(1)] = 1
		else:
			Error[reg.group(1)] += 1
		
		reg = re.search(r"ticky:\s*.*\s*([\w '?]+)\s*\((\w+)\)", line)
		ers = re.search(r"ticky:\s*ERROR\s*([\w '?]+)\s*\((\w+)\)", line)
		info = re.search(r"ticky:\s*INFO\s*([\w '?]+)\s*(\w+)", line)
		
		if reg is None:
			continue

		if reg.group(2) not in per_user.keys():
			per_user[reg.group(2)] = {}
			per_user[reg.group(2)]['INFO'] = 0
			per_user[reg.group(2)]['ERROR'] = 0

		if ers is not None:
			per_user[reg.group(2)]['ERROR'] += 1
		if info is not None:
			per_user[reg.group(2)]['INFO'] += 1
	
sorted_errors = sorted(Error.items(), key = operator.itemgetter(1), reverse = True)

sorted_per_user = sorted(per_user.items(), key = operator.itemgetter(0))


with open('error_message.csv', 'w') as efile:
	wObj = csv.writer(efile)
	wObj.writerow(["Error", "Count"])
	for e in sorted_errors:
		wObj.writerow(e)


with open('user_statistics.csv', 'w') as ucsv:
	wrObj = csv.writer(ucsv)
	wrObj.writerow(["Username", "INFO", "ERROR"])
	for u, d in sorted_per_user:
		wrObj.writerow([u, d["INFO"], d["ERROR"]])
