#!/bin/sh

FIFO=/web/omxfifo
if [ ! -f $FIFO ]
then
    mkfifo $FIFO
fi
killall -INT omxplayer.bin 2>/dev/null
/web/cls.sh
omxplayer -p -o hdmi "$1" < $FIFO > /tmp/omxplayer.log 2>&1 &
sleep 1
echo -n . > $FIFO

