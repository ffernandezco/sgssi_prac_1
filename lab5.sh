#!/bin/bash

origen=/home/lsi/seguridad
destino=/var/tmp/Backups

fecha=$(date +%F)

mkdir -p $destino/$fecha

rsync -a --link-dest=$destino/$(date -d yesterday +%F) $origen/ $destino/$fecha/

