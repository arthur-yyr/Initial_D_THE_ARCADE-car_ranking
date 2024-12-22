import os
import subprocess
from datetime import datetime, timezone, timedelta
import path

def file_copy():
    os.remove("rclone.log")
    subprocess.call("rclone copy Initial_D.xlsx gdrive:IniD --log-file=rclone.log --log-level DEBUG --config " + path.rclone_conf, shell=True)
    
    log_time = datetime.now(timezone(timedelta(hours=9))).isoformat(timespec='microseconds')
    with open("scheduler.log", "w+") as f:
        f.seek(0)
        f.truncate()
        f.write("Writing time: " + log_time)

if __name__ == "__main__":
    file_copy()
    print("\nFile Copied.\n")