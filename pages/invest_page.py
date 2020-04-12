"""
============================
Author:luli
Time:2020/4/11
Company:Happy
============================
"""
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class InvestPage(BasePage):
    # 输入框
    bid_input_locator = (By.CLASS_NAME, 'invest-unit-investinput')
    # 投标按钮
    bid_btn_locator = (By.CLASS_NAME, 'btn-special')
    # 投标成功弹窗
    bid_success_locator = (By.XPATH, '//div[@class="layui-layer-content"]//div[@class="capital_font1 note"]')
    # 投标失败弹窗
    bid_fail_locator = (By.XPATH, '//div[@class="layui-layer-content"]//div[@class="text-center"]')
    # 激活按钮元素
    bid_success_active_locator = (By.XPATH, "//div[@class='layui-layer-content']//button")

    def bid(self, money):
        # 1、定位金额输入框
        input_element = self.wait_presence(self.bid_input_locator)
        # 2、获取投标之前的余额
        money_before = input_element.get_attribute('data-amount')
        # 3、输入投标金额
        input_element.send_keys(money)
        # 4、定位投标按钮
        bid_btn = self.wait_clickable(self.bid_btn_locator)
        # 5、点击投标按钮
        bid_btn.click()
        # 6、返回投标前的金额
        return money_before

    def bid_success(self):
        e = self.wait_visible(self.bid_success_locator)
        return e.text

    def bid_fail(self):
        e = self.wait_visible(self.bid_fail_locator)
        return e.text

    def active_success(self):
        e = self.wait_clickable(self.bid_success_active_locator)
        e.click()
