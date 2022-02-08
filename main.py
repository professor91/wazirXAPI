from datetime import datetime

from handle_files import FileHandler
from wazirXAPI import WazirXAPI

filePath= "database/24hour/"
while True:
    if datetime.now().strftime("%x") == "00:00:00":
        # create new file
        newFile= FileHandler(filePath)
        file= newFile.createNewFile()
        del newFile
        print(f"log: created new file {newFile}")

        # get data from wazirX
        wazirX= WazirXAPI(file)
        wazirX.getMyTokensData()
        print(f"Fetched data from WazirX API and loaded in {file}")
        del wazirX