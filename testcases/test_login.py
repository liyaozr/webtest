"""
============================
Author:luli
Time:2020/4/6
Company:Happy
============================
"""
import unittest
from ddt import ddt, data
from selenium import webdriver
from pages.index import Index
from pages.login import Login
from datas.login_data import login_empty_param, login_invalid_param, login_success_param


@ddt
class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        # 隐式等待
        self.driver.implicitly_wait(20)

    def tearDown(self) -> None:
        self.driver.quit()

    @data(*login_empty_param)
    def test_empty_param(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果
        data = eval(test_info['data'])
        Login(self.driver).login(data['mobile'], data['pwd'])
        error_msg = Login(self.driver).get_error_msg()
        # 断言
        self.assertEqual(error_msg, expected)

    @data(*login_invalid_param)
    def test_invalid_param(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果
        data = eval(test_info['data'])
        Login(self.driver).login(data['mobile'], data['pwd'])
        invalid_msg = Login(self.driver).get_invalid_msg()
        # 断言
        self.assertEqual(invalid_msg, expected)

    @data(*login_success_param)
    def test_succs(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果
        data = eval(test_info['data'])
        Login(self.driver).login(data['mobile'], data['pwd'])
        succs_msg = Index(self.driver).get_mem_info()
        # 断言
        self.assertEqual(succs_msg, expected)
