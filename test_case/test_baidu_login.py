import unittest
import os
import time
import configparser
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

""" Created by xiaoxiaojing on 2018/8/22 """


def get_ini_data(section, key):
    try:
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        ini_path = project_path + "/Conf/config.ini"

        conf = configparser.ConfigParser()
        conf.read(ini_path, encoding="utf-8")
        print("即将访问：", conf.get(section, key))
        return conf.get(section, key)
    except Exception as err:
        print(err)


class TestBaiduLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("正在初始化……")
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_ini_data("Url", "baidu_url"))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("正在执行driver.quit()方法……")
        cls.driver.quit()

    # 验证是否成功登录，若登录成功，则退出账号
    def verify_and_logout(self):
        ele_usrname = self.driver.find_element_by_class_name("user-name")
        if ele_usrname.text == "22...4@qq.com":
            print("\n登录成功")

            # 退出登录
            ele_quit_btn = self.driver.find_element_by_class_name("quit")
            # 使用ActionChains获取动态元素
            ActionChains(self.driver).move_to_element(ele_usrname).click(ele_quit_btn).perform()
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="tip_con_wrap"]/div[3]/a[3]').click()

            if self.driver.find_element_by_xpath('//*[@id="u1"]/a[7]').text == "登录":
                print("已退出登录")
        else:
            print("登录失败")

    def test_login_with_password(self):

        time.sleep(1)
        # 进入用户名密码登录页面
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        ele = self.driver.find_element_by_xpath('//*[@id="TANGRAM__PSP_10__qrcode"]/p[1]')
        print("\n当前弹窗的title为：", ele.text)

        # 验证是否为用户名密码登录
        if ele.text in "扫码登录":
            self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()

        # 输入用户名密码登录
        self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(get_ini_data("Account", "tel"))
        self.driver.find_element_by_id("TANGRAM__PSP_10__password").send_keys(get_ini_data("Account", "passwd"))
        self.driver.find_element_by_id("TANGRAM__PSP_10__submit").click()

        if self.driver.find_element_by_id("TANGRAM__36__header_h3").text in "安全验证":
            time.sleep(1)
            self.driver.find_element_by_id("TANGRAM__36__button_send_mobile").click()

            mss_code = input("请输入短信验证码:")
            ele_input = self.driver.find_element_by_id("TANGRAM__36__input_vcode")

            ele_input.send_keys(mss_code)
            self.driver.find_element_by_id("TANGRAM__36__button_submit").click()

        self.verify_and_logout()

    def test_login_with_message(self):

        # 进入短信验证码登录页面
        self.driver.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
        ele = self.driver.find_element_by_class_name("pass-form-logo")
        print(ele.text)
        if ele.text in "扫码登录":
            self.driver.find_element_by_id("TANGRAM__PSP_10__footerULoginBtn").click()
        self.driver.find_element_by_id("TANGRAM__PSP_10__smsSwitchWrapper").click()

        # 验证是否为短信快捷登录
        ele = self.driver.find_element_by_class_name("pass-form-logo")
        self.assertIn(ele.text, "短信快捷登录", "当前页面不是短信快捷登录")

        # 输入手机号验证码登录
        self.driver.find_element_by_id("TANGRAM__PSP_10__smsPhone").send_keys(get_ini_data("Account", "tel"))
        self.driver.find_element_by_id("TANGRAM__PSP_10__smsTimer").click()
        message_code = input("请输入短信验证码：")
        self.driver.find_element_by_id("TANGRAM__PSP_10__smsVerifyCode").send_keys(message_code)
        self.driver.find_element_by_id("TANGRAM__PSP_10__smsSubmit").click()

        self.verify_and_logout()

    def test_test1(self):
        print(self.driver.page_source.__sizeof__())


if __name__ == '__main__':
    unittest.main()

