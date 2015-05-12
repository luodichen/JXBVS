# encoding=utf-8

'''
testing KeyValueConfigParser
'''
from utils import KeyValueConfigParser

kvcp = KeyValueConfigParser.KeyValueConfigParser("./login.defs")
result = kvcp.get_result()
print result
print 'PASS_MAX_DAYS = ' + result.get('PASS_MAX_DAYS')