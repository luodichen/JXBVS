# encoding=utf-8

'''
Created on May 13, 2015

@author: liuyonggang
'''

import sys
sys.path.append("../")
from BaseCheckPoint import BaseCheckPoint
from utils import KeyValueConfigParser


class LS0110000002(BaseCheckPoint):
    
    #定义检查项的标准值
    global normalValue
    normalValue = 6
    
    global checkFile
    #checkFile = "C:/etc/login.defs"
    checkFile = "/etc/login.defs"
    
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "LS0110000002"

    def check(self):
        global normalValue
        global checkFile
                
        kvcp = KeyValueConfigParser.KeyValueConfigParser(checkFile)
        try:
            result = kvcp.get_result()
            
            currentValue = result.get("PASS_MIN_DAYS")
            #print currentValue
            
            return {'checkPointID':self.get_id(), 'result':int(currentValue)>=normalValue}
        except:
            return {'checkPointID':self.get_id(), 'result':None}


