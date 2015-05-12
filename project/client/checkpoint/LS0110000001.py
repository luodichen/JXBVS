# encoding=utf-8
from BaseCheckPoint import BaseCheckPoint
import re

class LS0110000001(BaseCheckPoint):
    
    #定义检查项的标准值
    global normalValue
    normalValue = 90
    
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "LS0110000001"

    def check(self):
        global normalValue
        
        #打开配置文件并读取
        with open('/etc/login.defs', 'r') as checkFile:
        #with open('C:/etc/login.defs', 'r') as checkFile:
            fileContent = checkFile.read()
        
        #找出配置文件中未注释的符合要求的行       
        passMaxDaysString = re.findall('\n\s*#{0}\s*PASS_MAX_DAYS\s*\d+.*', fileContent)
        
        #根据正则表达式匹配的列表的，0个元素表示未匹配到，1个元素表示正常匹配，多个元素表示匹配出了多个，选择最后一个
        if len(passMaxDaysString) == 0:
            return {'checkPointID':self.get_id(), 'result':None}
        elif len(passMaxDaysString) == 1:
            #匹配出该配置的当前值并于标准值比较
            currentValue = re.findall('\d+', passMaxDaysString[0])
            if int(currentValue[0]) <= normalValue:
                return {'checkPointID':self.get_id(), 'result':True}
            else:
                return {'checkPointID':self.get_id(), 'result':False}
        else:
            listLen = len(passMaxDaysString)
            #匹配出该配置的当前值并于标准值比较
            currentValue = re.findall('\d+', passMaxDaysString[listLen-1])
            if int(currentValue[0]) <= normalValue:
                return {'checkPointID':self.get_id(), 'result':True}
            else:
                return {'checkPointID':self.get_id(), 'result':False}            
            

        


