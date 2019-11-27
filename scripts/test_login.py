import allure

from page.page_factory import Page_Factory
from utlis import init_driver, login_data
import pytest


class Test(object):
    def setup(self):
        self.driver = init_driver()
        self.page = Page_Factory(self.driver)

    def teardown(self):
        self.driver.quit()

    @pytest.mark.parametrize('name,pwd,expect,is_succ', login_data())
    def test_login_func(self, name, pwd, expect,is_succ):
        self.page.homepage.goto_mine()
        self.page.minepage.goto_login()
        self.page.loginpage.login_func(name, pwd)
        if is_succ:
            self.page.loginpage.click_login()
            self.page.loginpage.click_comf()
            nick_name = self.page.loginpage.get_nick_name()
            print('昵称是', nick_name)
            try:
                assert expect in nick_name
            except Exception as e :
                # 断言出错截图
                self.driver.get_screenshot_as_file('./screenshot/bug.png')
                # 打开截图生成的截图文件
                with open('./screenshot/bug.png','rb') as f:
                    allure.MASTER_HELPER.attach('断言失败截图',f.read(),allure.MASTER_HELPER.attach_type.PNG)
                raise e
        else:
            msg = self.page.loginpage.get_login_btn_attr('clickable')
            assert expect in msg
