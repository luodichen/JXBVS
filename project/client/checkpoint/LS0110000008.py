# encoding=utf-8

'''
Created on May 14, 2015

@author: liuyonggang
'''

import sys
sys.path.append("../")
from BaseCheckPoint import BaseCheckPoint

class LS0110000008(BaseCheckPoint):
    
    global checkFile
    checkFile = "C:/etc/passwd"
    #checkFile = "/etc/passwd"
    global valueTag
         
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "LS0110000008"

    def check(self):
        