# encoding=utf-8

'''
Created on May 18, 2015

@author: liuyonggang
'''

import sys
sys.path.append("../")
from BaseCheckPoint import BaseCheckPoint
from utils import KeyValueConfigParser

class LS0110000008(BaseCheckPoint):
    
    
    checkFile = "C:/etc/profile"
    #checkFile = "/etc/profile"
    stardandValue = 600
    
    checkMethod = "export"
    checkKey = "TIMEOUT"
         
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "LS0110000008"

    def check(self):
        mkvcp = KeyValueConfigParser.MethodKeyValueConfigParser(self.checkFile)
        try:
            currentValue = mkvcp.get_result(self.checkMethod, self.checkKey)
            #print currentValue
            if currentValue == None:
                return {'checkPointID':self.get_id(), 'result':False}
            elif int(currentValue) > self.stardandValue:
                return {'checkPointID':self.get_id(), 'result':False}
            else:
                return {'checkPointID':self.get_id(), 'result':True}               
        
        except:
            return {'checkPointID':self.get_id(), 'result':None}
            





        