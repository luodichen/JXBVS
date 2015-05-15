# encoding=utf-8

'''
Created on May 15, 2015

@author: luodichen
'''

'''
检查是否启用“不显示最后的用户名”策略
组策略位置：本地计算机策略\计算机配置\Windows设置\安全设置\本地策略\安全选项\交互式登录: 不显示最后的用户名
注册表位置：HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\dontdisplaylastusername
    0 - 已禁用, 1 - 已启用
'''
import sys
sys.path.append("../")
from BaseCheckPoint import BaseCheckPoint
import _winreg

class W12200000001(BaseCheckPoint):
    
    def __init__(self):
        BaseCheckPoint.__init__(self)
    
    def get_id(self):
        return "W12200000001"
    
    def check(self):
        result = None
        try:
            reg_key = _winreg.OpenKeyEx(_winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System")
            value, type = _winreg.QueryValueEx(reg_key, "dontdisplaylastusername")
            result = (1 == value)
        except:
            pass
        
        return {'checkPointID':self.get_id(), 'result':result}
    