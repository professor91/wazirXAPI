from wazirx_sapi_client.rest.client import Client
from json_db import jsdb

import time

class WazirXAPI():
    def __init__(self, _fileName):
        self.client= Client()
        self.jsdb_myTokens= jsdb("database/myTokens.json")
        self.file= jsdb(_fileName)
        # self.newFile= _fileName

    def getTokenData(self, _name: str):
        self.file.addItem(_name, self.client.send("ticker", {"symbol" : _name}))

    def getMyTokensData(self):
        for token in self.jsdb_myTokens._cacheddata.keys():
            self.getTokenData(token)
            time.sleep(1)

    # dont use
    def getAllData(self):
        self.jsdb_test._cacheddata= list(self.client.send("tickers"))[1]
        self.jsdb_test.dumpdata()
        # print(self.client.send("tickers"))

    def addNewToken(self, _name: str):
        self.jsdb_myTokens.addItem(_name, None)

obj= WazirXAPI("database/test.json")
obj.getMyTokensData()

# for item in obj.jsdb_myTokens._cacheddata.keys():
#     obj.getTokenData(item)
#     time.sleep(1)

# obj.getAllData()

del obj