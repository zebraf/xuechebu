from appium import webdriver
import yaml

def login_data():
    with open('./data/login_data.yml', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    return data

def init_driver():
    """驱动对象获取方法"""
    capabilities = {
        "platformName": "Android",
        "platformVersion": "5.1",
        "deviceName": "模拟器",
        "appPackage": "com.bjcsxq.chat.carfriend",
        "appActivity": ".MainActivity",
        # "noReset": True
    }
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=capabilities)
    return driver

# com.bjcsxq.chat.carfriend/.MainActivity

if __name__ == '__main__':
    init_driver()