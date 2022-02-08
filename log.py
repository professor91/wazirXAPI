from datetime import datetime

class CreateLog():
    #0. constructor
    def __init__(self, _filename: str):
        self.fileName= _filename

    #1. write log
    def log(self, _logfor: str, _logmessage: str):
        wf= open(self.fileName, "a")
        logtime= datetime.datetime.now().strftime("%x%l:%m:%S %p")
        wf.write(f"log @{logtime} for {_logfor}: {_logmessage}\n")
        wf.close()