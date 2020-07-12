#!/bin/sh
ssh root@192.168.99.106
cd /devt3/
if ls | grep *.html
then
if sudo ssh root@192.168.99.106 kubectl get deploy | grep html
then
echo "already running"
else
sudo ssh root@192.168.99.106 kubectl create -f /devt3/html.yml
fi
else
if sudo ssh root@192.168.99.106 kubectl get deploy | grep php
then
echo "already running"
else
sudo ssh root@192.168.99.106 kubectl create -f /devt3/php.yml
fi
fi