"""
登录页面
"""
import page
from base.basepage import BasePage


class LoginPage(BasePage):
    name = page.name
    pwd = page.pwd
    login_btn = page.login_btn
    com_btn = page.com_btn

    def login_func(self, name, pwd):
        self.input_func(self.name, name)
        self.input_func(self.pwd, pwd)
        self.click_func(self.login_btn)
        self.click_func(self.com_btn)
