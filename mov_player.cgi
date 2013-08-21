#!/usr/bin/python

print "Content-Type: text/html; charset=UTF8\n"


import cgi
form = cgi.FieldStorage()
parameter = form["title"].value
#print parameter
import subprocess
print subprocess.call(["echo /web/mov_player.sh " + parameter + "| at now"], shell=True)


