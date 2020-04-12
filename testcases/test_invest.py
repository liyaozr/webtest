"""
============================
Author:luli
Time:2020/4/11
Company:Happy
============================
"""
import time
import unittest
from decimal import Decimal
from ddt import data, ddt
from selenium import webdriver
from conf.secret_user import User
from datas.invest_data import invest_fail_data, invest_success_data
from pages.index_page import IndexPage
from pages.invest_page import InvestPage
from pages.login_page import LoginPage
from pages.user_page import UserPage

"""
1、登录
2、查看余额
3、输入投资金额
4、点击投资
5、查看余额
6、断言
"""


@ddt
class TestInvest(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        # 每个用例都需要登录
        LoginPage(self.driver).login(User.username, User.pwd)

    def tearDown(self) -> None:
        time.sleep(2)
        self.driver.quit()

    @data(*invest_fail_data)
    def test_invest_fail(self, test_info):
        # 1、登录之后进入首页，先在首页点击抢投标按钮
        IndexPage(self.driver).get_invest_btn()
        # 2、投标
        InvestPage(self.driver).bid(test_info['money'])
        # 3、获取实际结果
        fail_text = InvestPage(self.driver).bid_fail()
        print(fail_text)
        self.assertTrue(test_info['expected'] in fail_text)

    @data(*invest_success_data)
    def test_invest_success(self, test_info):
        # 1、登录之后进入首页，先在首页点击抢投标按钮
        IndexPage(self.driver).get_invest_btn()
        # 2、投标，并获取投标前的金额
        invest_page = InvestPage(self.driver)
        money_before = invest_page.bid(test_info['money'])
        success_text = invest_page.bid_success()
        self.assertTrue(test_info['expected'] in success_text)
        # 3、点击查看并激活
        invest_page.active_success()
        # 4、获取投标后的金额
        money_after = UserPage(self.driver).get_money()
        # 5、断言
        self.assertEqual(Decimal(money_before) - Decimal(str(test_info['money'])), Decimal(money_after))
