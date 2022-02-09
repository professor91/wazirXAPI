# global vars 
from log import CreateLogger
from json_db import jsdb

FileManager= jsdb("database/fileSystem.json")

db24hour_logger= CreateLogger(FileManager._cacheddata["logs"][0])
dbtest_logger= CreateLogger(FileManager._cacheddata["logs"][2])
mytokens_logger= CreateLogger(FileManager._cacheddata["logs"][1])