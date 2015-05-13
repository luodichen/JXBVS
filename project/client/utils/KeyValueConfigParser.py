# encoding=utf-8
'''
Created on May 12, 2015

@author: luodichen
'''

class KeyValueConfigParser(object):
    '''
    a key-value configure file parser
    
    sample file:
    ###### HERE IS A SIMPLE KEY-VALUE CONFIGURE FILE SAMPLE ######
    device_name        iPhone-6
    color              tuhao-gold #nice!
    price              $699
    
    result:
    {'device_name':'iPhone-6', 'color':'tuhao-gold', 'price':'$699'}
    
    '''
    
    STAT_PARSING_KEY = 0
    STAT_BLANKING = 1
    STAT_PARSING_VALUE = 2
    STAT_IN_COMMENT = 3
    STAT_IN_BLANK_LINE = 4
    
    read_file_path = ""
    cur_key = ""
    cur_value = ""
    status = STAT_IN_BLANK_LINE
    result = {}
    
    def __init__(self, file_path):
        self.read_file_path = file_path
        
    def put_new_record(self):
        self.result[self.cur_key] = self.cur_value
        self.cur_key = ""
        self.cur_value = ""
        
    def parse(self, word):
        if self.STAT_PARSING_KEY == self.status:
            if '#' == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_record()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                self.status = self.STAT_BLANKING
            else:
                self.cur_key = self.cur_key + word;
        elif self.STAT_BLANKING == self.status:
            if '#' == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                pass
            elif ' ' == word or '\t' == word:
                pass
            else:
                self.cur_value = self.cur_value + word
                self.status = self.STAT_PARSING_VALUE
        elif self.STAT_PARSING_VALUE == self.status:
            if '#' == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_record()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                pass
            else:
                self.cur_value = self.cur_value + word
        elif self.STAT_IN_COMMENT == self.status:
            if '\n' == word or '\r' == word:
                self.put_new_record()
                self.status = self.STAT_IN_BLANK_LINE
            else:
                pass
        elif self.STAT_IN_BLANK_LINE == self.status:
            if '#' == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                pass
            elif ' ' == word or '\t' == word:
                pass
            else:
                self.cur_key = self.cur_key + word;
                self.status = self.STAT_PARSING_KEY
            
    def get_result(self):
        with open(self.read_file_path, 'r') as file_obj:
            bufsize = 1024;
            while True:
                content = file_obj.read(bufsize)
                if len(content) == 0:
                    break
                
                for word in content:
                    self.parse(word)
        
        return self.result
    