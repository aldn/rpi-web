#!/bin/sh

RESOLVED_FILE=$(find /mnt/alice/MediaContent/video /mnt/alice/torrents -name *$@*)

/web/media_player.sh $RESOLVED_FILE
