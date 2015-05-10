from BaseCheckPoint import BaseCheckPoint

class SampleCheckPoint(BaseCheckPoint):
    
    def __init__(self):
        BaseCheckPoint.__init__(self)
        
    def get_id(self):
        return 1  # 填入定义好的CheckPoint ID
    
    def check(self):
        
        # 写入检查的相关代码
        
        # 返回时给Template程序时使用的格式
        return {'checkPointID':self.get_id(), 'result':True}
