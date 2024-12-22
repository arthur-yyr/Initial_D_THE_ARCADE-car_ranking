import schedule
import time
import main
from datetime import datetime, timezone, timedelta

if __name__ == "__main__":
    schedule.every().day.at("07:00").do(main.updatedata, sleeptime = 20)
    log_time = datetime.now(timezone(timedelta(hours=9))).isoformat(timespec='microseconds')
    with open("scheduler.log", "w+") as f:
        f.seek(0)
        f.truncate()
        f.write("Logging time: " + log_time)
    while True:
        schedule.run_pending()
        time.sleep(5)