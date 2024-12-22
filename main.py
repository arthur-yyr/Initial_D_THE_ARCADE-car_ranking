import data_download
import rank_count
import file_copy
from datetime import datetime, timezone, timedelta

def updatedata(sleeptime: int = 1):
    log_time = datetime.now(timezone(timedelta(hours=9))).isoformat(timespec='microseconds')
    with open("scheduler.log", "w+") as f:
        f.seek(0)
        f.truncate()
        f.write("Execution time: " + log_time)
    data_download.data_download(sleeptime)
    rank_count.rank_count()
    file_copy.file_copy()
    print("\nExecuted.\n")

if __name__ == "__main__":
    updatedata()
    