#!/usr/bin/python

print "Content-Type: text/html; charset=UTF8\n"

import cgi
import subprocess

def schedule(script, parameter):
    p = subprocess.Popen(['at', 'now'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    print p.communicate(input='/web/%s "%s"' % (script, parameter))[0]

form = cgi.FieldStorage()

if "title" in form.keys():
    schedule('mov_player.sh', form["title"].value)
elif "path" in form.keys():
    schedule('media_player.sh', form["path"].value)
