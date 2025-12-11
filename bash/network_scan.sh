#!/bin/bash
# Simple ping sweep network scanner

NETWORK="192.168.1"

echo "Scanning network $NETWORK.x ..."
for i in {1..254}
do
  ping -c 1 $NETWORK.$i > /dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "Host up: $NETWORK.$i"
  fi
done
