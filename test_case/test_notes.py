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
    try:
        # 项目地址
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        ini_path = project_path + "/Conf/config.ini"  # ini文件地址

        conf = configparser.ConfigParser()  # 定义读取ini文件的对象
        conf.read(ini_path, encoding="utf-8")  # 读取文件
        return conf.get(section, key)  # 获取指定value并返回
    except Exception as err:
        print(err)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_ini_data("Url", "baidu_url"))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def test_maxsize_window(self):  # 浏览器窗口最大化
        # self.driver.set_window_position(0, 0)
        # self.driver.maximize_window()  # 浏览器窗口最大化，mac上无法最大化
        self.driver.set_window_size(1400, 1000)
        print("windows尺寸为:", self.driver.get_window_size())  # 打印windows高和宽
        print("缓存为：", self.driver.get_cookies())  # 打印缓存
        print("缓存list取到第一字典中的value值：", self.driver.get_cookies()[0].get("value"))  # 打印缓存
        print("当前页面title为：", self.driver.title)
        print(self.driver.page_source)

    def test_test1(self):  # 使用ele.text进行断言

        self.driver.find_element_by_class_name("soutu-btn").click()
        upload_btn = self.driver.find_element_by_class_name("upload-text")

        if "本地上传图片" in upload_btn.text:  # 等价于下面的assertIn断言
            print("本地上传图片文本已找到")
        else:
            print("本地上传图片文本未找到")

        self.assertIn(upload_btn.text, "本地上传图片", "本地上传图片文本未找到")


if __name__ == '__main__':
    unittest.main()
