# from datetime import datetime

from libs.file_creator import FileCreator
from wazirXAPI import WazirXAPI

# while True:
    # if datetime.now().strftime("%x") == "00:00:00":

# create new file
fileCreator= FileCreator("database/24hour/")
file= fileCreator.create24hourFile()

# get data from wazirX
wazirX= WazirXAPI(file)
wazirX.getMyTokensData()
print(f"Fetched data from WazirX API and loaded in {file}")
del wazirX