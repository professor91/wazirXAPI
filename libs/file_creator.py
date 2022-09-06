from datetime import datetime
from libs.global_vars import FileManager
from libs.global_vars import db24hour_logger

# class for creating files
class FileCreator:
    def __init__(self, _pathtoFiles: str):
        # path to the directory to create file
        self.pathtoFiles= _pathtoFiles
    
    #1. initialize json filename
    #   given - NONE
    #   returns filename (as current_date.json)
    def fileName(self):
        return datetime.now().strftime("%d%b%Y")+".json"

    #2. creates new file
    #   given   - filename and file type
    #   returns - filename with full path
    def createNewFile(self, _fileName: str, _type: str):
        wf= open(self.pathtoFiles+_fileName, "w")
        
        if _type == "json":         # initialize json file
            wf.write("{}")
        elif _type == "txt":        # initialize text file
            wf.write("")
        else:                       # do not initialize file
            pass

        wf.close()
        del wf

        return self.pathtoFiles+_fileName

    #3. Function to create 24hour database json file    -   created for user
    #   given   - none
    #   returns - name of file with full path
    def create24hourFile(self):
        x= self.createNewFile(self.fileName(), "json")
        FileManager._cacheddata["database"]["24hour"].append(x)
        db24hour_logger.log(x, "Created new file")
        return x


# x= FileHandler("database/24hour/")
# x.createNewFile(x.fileName())
# print(x.listFiles())