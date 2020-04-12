"""
============================
Author:luli
Time:2020/4/11
Company:Happy
============================
"""

import os
import time
import logging

import pyperclip
import pyautogui as ui
from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from conf import Setting


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver
        self.driver.maximize_window()

    def screenshot(self):
        img_path = Setting.img_path
        filename = str(int(time.time())) + '.png'
        file = os.path.join(img_path, filename)
        self.driver.save_screenshot(file)

    def get_element(self, locator):
        """查找元素"""
        try:
            e = self.driver.find_element(*locator)
            return e
        except Exception as E:
            logging.error('查找元素失败')
            self.screenshot()

    def wait_clickable(self, locator, timeout=30, poll=0.2):
        """等待元素可被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(EC.element_to_be_clickable(locator))
            return e
        except:
            logging.error('查找元素失败')
            self.screenshot()

    def wait_presence(self, locator, timeout=30, poll=0.2):
        """等待元素可被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(EC.presence_of_element_located(locator))
            return e
        except:
            logging.error('查找元素失败')
            self.screenshot()

    def wait_visible(self, locator, timeout=30, poll=0.2):
        """等待元素可被点击"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(EC.visibility_of_element_located(locator))
            return e
        except:
            logging.error('查找元素失败')
            self.screenshot()

    def wait_iframe(self, locator, timeout=30, poll=0.2):
        """等待ifram可切换"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(EC.frame_to_be_available_and_switch_to_it(locator))
            return e
        except:
            logging.error('切换iframe失败')
            self.screenshot()

    def wait_windows(self, element, timeout=30, poll=0.2):
        """等待窗口可切换"""
        try:
            windows = self.driver.window_handles
            element.click()
            WebDriverWait(self.driver, timeout, poll).until(EC.new_window_is_opened(windows))
            self.driver.switch_to.window(self.driver.window_handles[-1])
        except:
            logging.error('切换窗口失败')
            self.screenshot()

    def wait_select(self, locator, value, timeout=30, poll=0.2):
        """等待元素可选择"""
        try:
            e = WebDriverWait(self.driver, timeout, poll).until(EC.element_located_to_be_selected(locator))
            select = Select(e)
            select.select_by_value(value)
        except:
            logging.error('选择元素失败')
            self.screenshot()

    def handle_window_scroll(self, locator):
        """等待窗口将元素滚动到可见区域"""
        try:
            e = self.get_element(locator)
            e.location_once_scrolled_into_view()
            return e
        except:
            logging.error('元素滚动失败')
            self.screenshot()

    def handle_file(self, locator, file):
        try:
            e = self.get_element(locator)
            e.click()
            pyperclip.copy(file)
            time.sleep(2)
            ui.hotkey('ctrl', 'v')
            time.sleep(2)
            ui.press('enter', presses=2)
        except:
            logging.error('文件上传失败')
            self.screenshot()
