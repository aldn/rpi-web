#!/usr/bin/python

print "Content-Type: text/html; charset=UTF8\n"


import os
import cgi
from struct import pack

form = cgi.FieldStorage()
parameter = form["id"].value

command_map = dict()
command_map['pause']             = 'p'
command_map['stop']              = 'q'
command_map['volup']             = '+'
command_map['voldown']           = '-'
command_map['seek-30']           = pack('>H',0x5b44)
command_map['seek30']            = pack('>H',0x5b43)
command_map['seek-600']          = pack('>H',0x5b42)
command_map['seek600']           = pack('>H',0x5b41)
command_map['speedup']           = '1'
command_map['speeddown']         = '2'
command_map['nextchapter']       = 'o'
command_map['prevchapter']       = 'i'
command_map['nextaudio']         = 'k'
command_map['prevaudio']         = 'j'
command_map['togglesubtitles']   = 's'
command_map['nextsubtitles']     = 'm'
command_map['prevsubtitles']     = 'n'


fd_control_fifo = os.open('omxfifo', os.O_WRONLY | os.O_NONBLOCK)
os.write(fd_control_fifo, command_map[parameter])
os.close(fd_control_fifo)

