#!python

'''
testing KeyValueConfigParser
'''

import sys
sys.path.append("../../")
from utils import KeyValueConfigParser

mkvcp = KeyValueConfigParser.MethodKeyValueConfigParser("C:/etc/xxx")

print mkvcp.get_result("export", "TIMEOUT")


