#!/usr/bin/env python3
import os
import shutil
from datetime import datetime

SOURCE = "/home/user/documents"      # Replace with your preferred path
DEST = "/home/user/cloud_backup"     # Simulated cloud bucket folder

print("===== CLOUD BACKUP UPLOADER =====")
print("Starting backup...")

if not os.path.exists(DEST):
    os.makedirs(DEST)

date = datetime.now().strftime("%Y-%m-%d")
backup_name = f"backup-{date}.zip"

shutil.make_archive(f"/tmp/{backup_name}", 'zip', SOURCE)
shutil.move(f"/tmp/{backup_name}.zip", DEST)

print(f"Backup complete: {backup_name}")
print(f"Saved to: {DEST}")
