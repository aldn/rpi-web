#!/bin/sh

FIFO=/web/omxfifo
if [ ! -f $FIFO ]
then
    mkfifo $FIFO
fi
killall -INT omxplayer.bin 2>/dev/null
/web/cls.sh
omxplayer -o hdmi "$@" < $FIFO > /dev/null 2>&1 &
sleep 1
echo -n . > $FIFO

