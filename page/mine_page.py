"""
我的页面
"""
import page
from base.basepage import BasePage


class MinePage(BasePage):
    login = page.login

    def goto_login(self):
        self.click_func(self.login, 10)
