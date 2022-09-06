from datetime import datetime
import schedule

from libs.file_creator import FileCreator
from wazirXAPI import WazirXAPI

fileCreator= FileCreator("database/24hour/")

def job():
    file= fileCreator.create24hourFile()    # create new file
    wazirX= WazirXAPI(file)
    wazirX.getMyTokensData()                # get data from wazirX
    print(f"Fetched data from WazirX API and loaded in {file}")
    del wazirX

schedule.every().day.at("00:00").do(job)

while True:
    schedule.run_pending()
