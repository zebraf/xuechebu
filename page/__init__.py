from selenium.webdriver.common.by import By

# 主页面
mine = By.XPATH, "//*[contains(@text,'我的')]"
# 我的页面
login = By.XPATH, '//*[contains(@text,"登录")]'
# 登录页面
name = By.XPATH, '//*[contains(@text,"请输入手机")]'  # 账号
pwd = By.ID, 'com.bjcsxq.chat.carfriend:id/login_pwd_et'  # 密码
login_btn = By.ID, 'com.bjcsxq.chat.carfriend:id/login_btn'  # 登录按钮
com_btn = By.XPATH, '//*[contains(@text,"确定")]'  # 登录提示框确定按钮
