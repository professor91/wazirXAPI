from datetime import datetime
import os

# class for managing creation of files
class FileHandler:
    #0. constructor
    def __init__(self, _pathofFiles: str):
        self.index= None
        self.pathofFiles= _pathofFiles
    
    #1. initialize json filename as date when file is created
    def fileName(self):
        return datetime.now().strftime("%d%b%Y")+".json"

    #2. create file with the given name at the path mentioned in self.pathofFiles
    def createNewFile(self, _fileName: str):
        wf= open(self.pathofFiles+_fileName, "w")
        wf.write("{}")
        wf.close()
        print(f"log: created new file at path {self.pathofFiles+_fileName}")
        return self.pathofFiles+_fileName
    
    #3. return list of files in the directory  
    def listFiles(self):
        return os.listdir(self.pathofFiles)

x= FileHandler("database/24hour/")
# x.createNewFile(x.fileName())
# print(x.listFiles())