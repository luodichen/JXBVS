# encoding=utf-8
'''
Created on May 12, 2015

@author: luodichen
@author: liuyonggang
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


class MethodKeyValueConfigParser(object):
    '''
    a method-key-value configure file parser
    
    sample file:
    ###### HERE IS A SIMPLE METHOD-KEY-VALUE CONFIGURE FILE SAMPLE ######
    export TIMEOUT=600
    export    TIMEOUT=600
        export TIMEOUT=600
     export TIMEOUT=600
    export TIMEOUT    = 600
    
    result "value"
    
    '''
    
    STAT_PARSING_METHOD   = 0              #解析method
    STAT_PARSING_KEY = 1                          #解析key
    STAT_PARSING_VALUE = 2                    #解析value
    STAT_BLANKING = 3    #Method与key之间的空白
    STAT_IN_COMMENT = 4                          #在注释中
    STAT_IN_BLANK_LINE = 5                        #在（连续的）空行中
    STAT_IN_ERROR = 6           #遇到多个等于号
    
    read_file_path = ""
    status = STAT_IN_BLANK_LINE
    blank_tag = 0   #
    equal_num = 0 
    result = []
    cur_method = ""
    cur_key = ""
    cur_value = ""
    
    def __init__(self, file_path):
        self.read_file_path = file_path
    
    def put_new_recode(self):
        self.result.append((self.cur_method, self.cur_key, self.cur_value))
        self.cur_method = ""
        self.cur_key = ""
        self.cur_value = ""
        self.blank_tag = 0  #method之前，1 method与key之间 ，2 key与“=”之间， 3 “=”之后，value之前 ，4value之后
    
    def parse(self, word):
        if self.STAT_PARSING_METHOD == self.status:
            if "#" == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_recode()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                self.status = self.STAT_BLANKING
                self.blank_tag = 1
            elif '=' == word:
                self.status = self.STAT_IN_ERROR
            else:
                self.cur_method = self.cur_method + word
        
        elif self.STAT_PARSING_KEY == self.status:
            if "#" == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_recode()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                self.status = self.STAT_BLANKING
                self.blank_tag = 2
            elif '=' == word:
                self.status = self.STAT_BLANKING
                self.blank_tag = 3
            else:
                self.cur_key = self.cur_key + word
        
        elif self.STAT_PARSING_VALUE == self.status:
            if "#" == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_recode()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                pass
            elif '=' == word:
                self.status = self.STAT_IN_ERROR
            else:
                self.cur_value = self.cur_value + word
        
        elif self.STAT_BLANKING == self.status:
            if "#" == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                self.put_new_recode()
                self.status = self.STAT_IN_BLANK_LINE
            elif ' ' == word or '\t' == word:
                pass
            elif '=' == word:
                if self.blank_tag == 2:
                    self.blank_tag = 3
                else:
                    self.status = self.STAT_IN_ERROR
            else:
                if self.blank_tag == 0:
                    self.cur_method = self.cur_method + word
                    self.status = self.STAT_PARSING_METHOD
                elif self.blank_tag == 1:
                    self.cur_key = self.cur_key + word
                    self.status = self.STAT_PARSING_KEY
                elif self.blank_tag == 2:
                    self.status = self.STAT_IN_ERROR
                elif self.blank_tag == 3:
                    self.cur_value = self.cur_value + word
                    self.status = self.STAT_PARSING_VALUE
                else:
                    pass
        
        elif self.status == self.STAT_IN_COMMENT:
            if '\n' == word or '\r' == word:
                self.status = self.STAT_IN_BLANK_LINE
            else:
                pass
        
        elif self.status == self.STAT_IN_BLANK_LINE:
            if '#' == word:
                self.status = self.STAT_IN_COMMENT
            elif '\n' == word or '\r' == word:
                pass
            elif ' ' == word or '\t' == word:
                self.status = self.STAT_BLANKING
                self.blank_tag = 0
            elif '=' == word:
                self.status = self.STAT_IN_ERROR
            else:
                self.cur_method = self.cur_method + word
                self.status = self.STAT_PARSING_METHOD
        
        elif self.status == self.STAT_IN_ERROR:
            if '\n' == word or '\r' == word:
                self.put_new_recode()
                self.STAT_IN_BLANK_LINE
            else:
                pass                            
                
        
            
    def get_result(self, nMethod, nKey):
        with open(self.read_file_path, 'r') as file_obj:
            bufsize = 1024
            
            while True:
                content = file_obj.read(bufsize)
                if len(content) == 0:
                    break
                
                for word in content:
                    self.parse(word)
        
        for tmpList in self.result:
            
            tmpMethod, tmpKey, tmpValue = map(None, tmpList)
            if tmpMethod == nMethod and tmpKey == nKey:
                return tmpValue                                                         
    
        return None
        
        
        