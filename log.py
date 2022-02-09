from datetime import datetime

class CreateLogger():
    def __init__(self, _filename: str):
        self.file= "logs/"+_filename

    #1. write log
    def log(self, _logfor: str, _logmessage: str):
        wf= open(self.file, "a")

        logtime= datetime.now().strftime("%x%l:%m:%S %p")
        wf.write(f"log @ {logtime} for {_logfor}: {_logmessage}\n")
        
        wf.close()
        del wf