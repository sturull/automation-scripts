#!/usr/bin/env python3
import platform
import psutil

print("===== SYSTEM INFORMATION =====")
print(f"System: {platform.system()}")
print(f"Node Name: {platform.node()}")
print(f"Release: {platform.release()}")
print(f"Version: {platform.version()}")
print(f"Machine: {platform.machine()}")
print(f"Processor: {platform.processor()}")

print("\n===== CPU INFO =====")
print("Cores:", psutil.cpu_count(logical=False))
print("Threads:", psutil.cpu_count(logical=True))

print("\n===== MEMORY =====")
mem = psutil.virtual_memory()
print(f"Total: {mem.total / (1024**3):.2f} GB")
print(f"Used: {mem.used / (1024**3):.2f} GB")
print(f"Available: {mem.available / (1024**3):.2f} GB")

print("\n===== DISK USAGE =====")
disk = psutil.disk_usage('/')
print(f"Total: {disk.total / (1024**3):.2f} GB")
print(f"Used: {disk.used / (1024**3):.2f} GB")
print(f"Free: {disk.free / (1024**3):.2f} GB")
