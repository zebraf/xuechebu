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
    nick_name = page.nick_name

    def login_func(self, name, pwd):
        self.input_func(self.name, name)
        self.input_func(self.pwd, pwd)
    def click_login(self):
        self.click_func(self.login_btn)
    def click_comf(self):
        self.click_func(self.com_btn)

    def get_nick_name(self):
        return self.find_ele(self.nick_name).text

    def get_login_btn_attr(self,attr_name):
        return self.get_attruibute_func(self.login_btn,attr_name)
