#!/usr/bin/python

print "Content-Type: text/html; charset=UTF8\n"

import cgi
import subprocess

form = cgi.FieldStorage()
if "title" in form.keys():
    param_title = form["title"].value
    print subprocess.call(['echo /web/mov_player.sh \\"%s\\" | at now' % param_title], shell=True)
elif "path" in form.keys():
    param_path = form["path"].value
    print param_path
    print subprocess.call(['echo /web/media_player.sh \\"%s\\" | at now' % param_path], shell=True)
