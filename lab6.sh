#!/bin/bash

SOURCE_DIR=/home/lsi/Seguridad/
BACKUP_DIR=/var/tmp/Backups

DATETIME=$(date +%F)

BACKUP_PATH=$BACKUP_DIR/$DATETIME
LATEST_LINK=$BACKUP_DIR/$(date -d yesterday +%F)


ssh -i /home/user/.ssh/clave usuario@ip-remota mkdir -p $BACKUP_PATH
ssh usuario@ip-remota mkdir -p $LATEST_LINK

rsync -a -e "ssh -i /home/user/.ssh/sshgakopribatu" --link-dest=$LATEST_LINK $SOURCE_DIR usuario@ip-remota:$BACKUP_PATH

