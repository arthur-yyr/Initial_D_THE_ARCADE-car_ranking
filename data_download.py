from datetime import datetime, timezone, timedelta
import time
import os
import requests
import course_url

def data_download(sleeptime: int = 1):
    # Create folder if not exist
    os.makedirs('courses', exist_ok=True)

    # Download and Save as json file
    course_count = course_url.course_list_len
    for i in range(0, course_count):
        course, url = course_url.get_course_and_url(i)
        filename = course + ".json"
        jsondata = requests.get(url)
        with open("courses/" + filename, "wb") as f:
            f.seek(0)
            f.truncate()
            f.write(jsondata.content)
        time.sleep(sleeptime)
    
if __name__ == "__main__":
    print("\nThis is the script used to download the json files of ranking.\n")
    data_download()
