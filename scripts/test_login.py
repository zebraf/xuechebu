from page.page_factory import Page_Factory
from utlis import init_driver, login_data
import pytest


class Test(object):
    def setup(self):
        self.driver = init_driver()
        self.page = Page_Factory(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,pwd', login_data())
    def test_login_func(self, name, pwd):
        self.page.homepage.goto_mine()
        self.page.minepage.goto_login()
        self.page.loginpage.login_func(name, pwd)
