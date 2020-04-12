"""
============================
Author:luli
Time:2020/4/6
Company:Happy
============================
"""
import time

from selenium.webdriver.common.by import By
from common.base_page import BasePage
from conf import Setting


class LoginPage(BasePage):
    user_locator = (By.NAME, 'phone')
    pwd_locator = (By.NAME, 'password')
    btn_locator = (By.XPATH, "//button[@class='btn btn-special']")
    error_locator = (By.CLASS_NAME, 'form-error-info')
    invalid_locator = (By.CLASS_NAME, 'layui-layer-content')

    def get_login(self):
        """获取登录页面"""
        # 为什么单独拿出来，因为有可能只需要进入登录这个页面，不需要进行登录等操作
        url = Setting.host + Setting.login_url
        self.driver.get(url)

    def login(self, username, password):
        """登录"""
        self.get_login()
        # 定位用户名
        user_ele = self.get_element(self.user_locator)
        # 输入用户名
        user_ele.send_keys(username)
        # 定位密码
        pwd_ele = self.get_element(self.pwd_locator)
        # 输入密码
        pwd_ele.send_keys(password)
        # 定位登录按钮
        login_btn = self.get_element(self.btn_locator)
        # 点击登录按钮
        login_btn.click()

    def get_error_msg(self):
        """获取错误信息"""
        error_ele = self.wait_visible(self.error_locator)
        return error_ele.text

    def get_invalid_msg(self):
        """获取未授权信息"""
        invalid_ele = self.wait_visible(self.invalid_locator)
        return invalid_ele.text
