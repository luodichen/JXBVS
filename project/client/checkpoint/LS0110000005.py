# encoding=utf-8

'''
Created on May 14, 2015

@author: liuyonggang
'''

import sys
sys.path.append("../")
from BaseCheckPoint import BaseCheckPoint

class LS0110000005(BaseCheckPoint):
    
    global checkFile
    #checkFile = "C:/etc/shadow"
    checkFile = "/etc/shadow"
    global valueTag
         
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "LS0110000005"

    def check(self):
        global checkFile
        try:
            myFile = open(checkFile, 'r')
            for fileLine in myFile.readlines():
                fileLineContentList = fileLine.split(':')
                if fileLineContentList[1] == '!' :
                    return {'checkPointID':self.get_id(), 'result':False}
            return {'checkPointID':self.get_id(), 'result':True}               
            
        except:
            return {'checkPointID':self.get_id(), 'result':None}
    
    
