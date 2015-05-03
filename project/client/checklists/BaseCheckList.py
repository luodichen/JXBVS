
class BaseCheckList(object):
    
    id = 0
    
    def __init__(self):
        self.id = self.get_id()
    
    def get_id(self):
        pass
    
    def check(self):
        pass