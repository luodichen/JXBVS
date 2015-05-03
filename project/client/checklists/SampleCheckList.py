import BaseCheckList

class SampleCheckList(BaseCheckList):
    def __init__(self):
        pass
        
    def get_id(self):
        return 1 # sample checklist id
    
    def check(self):
        print id