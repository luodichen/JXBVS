from BaseCheckList import BaseCheckList

class SampleCheckList(BaseCheckList):
    def __init__(self):
        BaseCheckList.__init__(self)
        
    def get_id(self):
        return 1 # sample checklist id
    
    def check(self):
        return {'id':self.get_id(), 'result':True}
