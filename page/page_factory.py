"""
page工厂
"""
from page.home_page import HomePage
from page.login_page import LoginPage
from page.mine_page import MinePage


class Page_Factory(object):
    def __init__(self, driver):
        self.driver = driver

    @property
    def homepage(self):
        return HomePage(self.driver)

    @property
    def minepage(self):
        return MinePage(self.driver)

    @property
    def loginpage(self):
        return LoginPage(self.driver)
