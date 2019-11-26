"""
主页面
"""
import page
from base.basepage import BasePage


class HomePage(BasePage):
    mine = page.mine

    def goto_mine(self):
        self.click_func(self.mine, 10)
