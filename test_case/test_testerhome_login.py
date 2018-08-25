import unittest
import os
import time
import configparser
from selenium import webdriver

""" Created by xiaoxiaojing on 2018/8/23 """


def get_ini_data(section, key):
    progect_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ini_path = progect_path + "/Conf/config.ini"

    conf = configparser.ConfigParser()
    conf.read(ini_path, encoding="utf-8")
    print("\n已从ini文件成功取到：", conf.get(section, key))
    return conf.get(section, key)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("正在初始化……")
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_ini_data("Url", "testerhome_url"))
        # cls.driver.implicitly_wait(3)

    @classmethod
    def tearDownClass(cls):
        print("\n正在执行driver.quit()方法")
        # cls.driver.quit()

    def test_a_login_checklogin(self):
        """
        断言相等性 driver.title 测试场景
        断言相等性 driver.current_url
        <非必要条件>判断网页源码 尺寸大小 不高于60kb 如果不满足写入文件 /test/size.txt
        判断前往登录元素是否可以点击
        断言相等性 登录元素文本正确
        """
        time.sleep(1)
        try:
            self.assertEqual(self.driver.title, "TesterHome",
                             msg="\n{}与TesterHome不相等".format(self.driver.title))
            self.assertEqual(self.driver.current_url, "https://testerhome.com/",
                             msg="\n{}与https://testerhome.com/不相等".format(self.driver.current_url))

            page_size = self.driver.page_source.__sizeof__()
            if int(page_size / 1024) > 60:
                file = open("../file/sizelog.txt", "w", encoding="utf=8")
                file.write("{}页面size太大，建议优化".format(self.driver.current_url))
                file.close()

            ele_login = self.driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul[1]/li[2]/a')
            if ele_login.is_enabled():
                self.assertEqual(ele_login.text, "登录")
                ele_login.click()
                time.sleep(2)
            else:
                print("登录不可点击")

        except Exception as err:
            print(err)

    def test_b_login(self):

        self.assertEqual(self.driver.title, "登录 · TesterHome")

        # 输入用户名密码，勾选记住登录状态，登录
        self.driver.find_element_by_id("user_login").send_keys(get_ini_data("Testerhome", "username"))
        time.sleep(1)
        self.driver.find_element_by_id("user_password").send_keys(get_ini_data("Testerhome", "password"))
        time.sleep(1)
        self.driver.find_element_by_id("user_remember_me").click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="new_user"]/div[4]/input').click()

    def test_c_logout(self):

        time.sleep(2)
        ele_news = self.driver.find_element_by_class_name("count")
        if ele_news:
            print("\n登录成功")
            print("\n新消息数为：", ele_news.text)

        # 退出登录
        time.sleep(1)
        self.driver.find_element_by_class_name("dropdown-toggle").click()
        self.driver.find_element_by_xpath('/html/body/div[1]/nav/div/ul[1]/li/ul/li[7]/a').click()

        self.assertEqual(self.driver.current_url, "https://testerhome.com/topics",
                         msg="当前url {} 与 https://testerhome.com/topics 不想等，退出登录未成功")


if __name__ == '__main__':
    unittest.main()
