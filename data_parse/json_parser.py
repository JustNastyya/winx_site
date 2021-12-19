import json
from json import decoder
import os
import io

class JsonParser():
    def __init__(self, info):
        #with io.open(dir, encoding='utf-8', mode='r') as jsonFile:
        #    self.info = json.load(jsonFile)
        #    jsonFile.close()
        self.info = info
    
    def get_feie(self, name):
        return self.info[name]
    
    def get_all(self):
        return self.info
