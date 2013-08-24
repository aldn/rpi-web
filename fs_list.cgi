#!/usr/bin/python

print "Content-Type: text/html; charset=UTF8\n"

import os
import cgi
import json

form = cgi.FieldStorage()
parameter = form["path"].value

response = []

items = os.listdir(parameter)

files = []
dirs = []

for item in items:
    if not item.startswith('.'):
        if os.path.isdir(os.path.join(parameter, item)):
            dirs.append(item)
        else:
            files.append(item)
files = sorted(files, key=lambda s: s.lower())
dirs = sorted(dirs, key=lambda s: s.lower())

for d in dirs:
    response.append( { 'name' : d, 'is_dir' : True } )
for f in files:
    response.append( { 'name' : f, 'is_dir' : False } )

print json.dumps(response, sort_keys=True, indent=4, separators=(',', ': '))
