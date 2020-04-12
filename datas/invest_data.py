"""
============================
Author:luli
Time:2020/4/11
Company:Happy
============================
"""

invest_fail_data = [
    {'money': -100, 'expected': '请正确填写投标金额'},
    {'money': 0, 'expected': '请正确填写投标金额'},
    {'money': 500000, 'expected': '购买标的金额不能大于标剩余金额'},
    {'money': 20000000000, 'expected': '投标金额大于可用金额'}
]

invest_success_data = [
    {'money': 200, 'expected': '投标成功'},
]
