#!/bin/bash
# System Health Check Script
# Provides quick CPU, memory, disk, and process info.

echo "===== SYSTEM HEALTH CHECK ====="
echo "Date: $(date)"
echo ""

echo "--- CPU Load ---"
uptime
echo ""

echo "--- Memory Usage ---"
free -h
echo ""

echo "--- Disk Usage ---"
df -h /
echo ""

echo "--- Top 5 Processes ---"
ps aux --sort=-%cpu | head -n 6
echo ""
