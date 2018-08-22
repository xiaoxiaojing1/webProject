import unittest
import os
import configparser
import time
from selenium import webdriver


def get_ini_data(section, key):
    """关键字驱动
      :param section: ini类型文件.section
      :param key: get.key =>value
      :return: str
      """
    project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    ini_path = project_path + "/Conf/config.ini"

    conf = configparser.ConfigParser()
    conf.read(ini_path, encoding="utf-8")
    return conf.get(section, key)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_ini_data("Url", "baidu_url"))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        pass

    def test_maxsize_window(self):  # 浏览器窗口最大化
        # self.driver.set_window_position(0, 0)
        # self.driver.maximize_window()  # 浏览器窗口最大化，mac上无法最大化
        self.driver.set_window_size(1400, 1000)
        time.sleep(3)
        print("windows尺寸为:", self.driver.get_window_size())  # 打印windows高和宽
        print("缓存为：", self.driver.get_cookies())  # 打印缓存
        print("当前页面title为：", self.driver.title)
        print(self.driver.page_source)


if __name__ == '__main__':
    unittest.main()
