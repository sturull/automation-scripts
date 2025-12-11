#!/bin/bash
# Log cleaner script
# Deletes log files older than 14 days from /var/log/custom/

LOGDIR="/var/log/custom"

echo "Cleaning logs older than 14 days in $LOGDIR..."
find $LOGDIR -type f -mtime +14 -exec rm -f {} \;

echo "Cleanup complete."
