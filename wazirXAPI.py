from wazirx_sapi_client.rest.client import Client
from json_db import jsdb

from global_vars import mytokens_logger
from global_vars import db24hour_logger

import time

class WazirXAPI():
    def __init__(self, _pathtoFile : str):
        self.client= Client()
        self.jsdb_myTokens= jsdb("database/myTokens.json")
        self.jsdb_test= jsdb("database/test.json")
        self.pathtoFile= _pathtoFile
        self.jsdb_file= jsdb(_pathtoFile)

    #1. get token 24 hour data from wazirX
    #   given   - symbol of the token
    #   returns - None
    def getTokenData(self, _symbol: str):
        self.jsdb_file.addItem( _symbol, 
                                self.client.send("ticker", {"symbol" : _symbol})[1])

    #2. get data of all my tokens
    #   given   - None
    #   returns - None
    def getMyTokensData(self):
        for token in self.jsdb_myTokens._cacheddata.keys():
            self.getTokenData(token)
            time.sleep(1)
        db24hour_logger.log(self.pathtoFile, "Fetched data for my tokens")

    #3. add new token to myTokens.json
    #   given   - symbol of the token
    #   returns - None
    def addNewToken(self, _symbol: str):
        self.jsdb_myTokens.addItem(_symbol, None)
        mytokens_logger.log("database/myTokens", "Added new token to myToken dict")

    # dont use
    def getAllData(self):
        self.jsdb_test._cacheddata= list(self.client.send("tickers"))[1]
        self.jsdb_test.dumpdata()
        # print(self.client.send("tickers"))
        print("got all data")



obj= WazirXAPI("database/test.json")
obj.getAllData()

del obj