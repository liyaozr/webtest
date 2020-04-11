"""
============================
Author:luli
Time:2020/4/10
Company:Happy
============================
"""

login_empty_param = [
    {"mobile": "", "pwd": "123456", "expected": "请输入手机号"},
    {"mobile": "18675467432", "pwd": "", "expected": "请输入密码"},
]

login_invalid_param = [
    {"mobile": "18745678943", "pwd": "123456", "expected": "此账号没有经过授权，请联系管理员!"},
    {"mobile": "18675467432", "pwd": "12345678", "expected": "帐号或密码错误!"},
]

login_success_param = [
    {"mobile": "18684720553", "pwd": "python", "expected": "我的帐户[华华]"}
]

