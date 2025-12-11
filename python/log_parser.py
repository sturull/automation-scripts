#!/usr/bin/env python3
# Simple log parser for security or system logs

log_file = "/var/log/syslog"  # You can change this

print("===== LOG PARSER =====")
print(f"Reading from: {log_file}")

try:
    with open(log_file, "r") as f:
        for line in f:
            if "error" in line.lower() or "fail" in line.lower():
                print(line.strip())
except FileNotFoundError:
    print("Log file not found. Try a different path.")
