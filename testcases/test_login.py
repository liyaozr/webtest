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
from pages.index_page import IndexPage
from pages.login_page import LoginPage
from datas.login_data import login_empty_param, login_invalid_param, login_success_param


@ddt
class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = webdriver.Chrome()
        # 隐式等待
        cls.driver.implicitly_wait(30)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    @data(*login_empty_param)
    def test_empty_param(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果

        LoginPage(self.driver).login(test_info['mobile'], test_info['pwd'])
        error_msg = LoginPage(self.driver).get_error_msg()
        # 断言
        self.assertEqual(error_msg, expected)

    @data(*login_invalid_param)
    def test_invalid_param(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果
        LoginPage(self.driver).login(test_info['mobile'], test_info['pwd'])
        invalid_msg = LoginPage(self.driver).get_invalid_msg()
        # 断言
        self.assertEqual(invalid_msg, expected)

    @data(*login_success_param)
    def test_succs(self, test_info):
        # 获取预期结果
        expected = test_info['expected']
        # 获取实际结果
        LoginPage(self.driver).login(test_info['mobile'], test_info['pwd'])
        succs_msg = IndexPage(self.driver).get_mem_info()
        # 断言
        self.assertEqual(succs_msg, expected)
