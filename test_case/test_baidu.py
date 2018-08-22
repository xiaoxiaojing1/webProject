import os
import time
import configparser
import unittest
from selenium import webdriver


currentPath = os.path.abspath(os.path.dirname(__file__))  # 当前文件夹目录
currentPath2 = os.path.dirname(__file__)
# print(__file__)  # 1__file__
# print(os.path.abspath("test_baidu.py"))  # 2abspath()
# print(currentPath2)  # 3dirname()
# print(currentPath)  # 4dirname()+abspath()
#
# print("\n", os.path.join(currentPath2, ".."))  # 5join
# print(os.path.abspath(os.path.join(currentPath2, "..")))  # 6将join结果进行abspath
#
# print("\n", os.path.split(currentPath))  # 7split()


def path_ini():
    pathobj = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+"/Conf/config.ini"
    # __file__ == /Users/hxj/PycharmProjects/webProject/test_case/test_baidu.py
    # os.path.dirname(__file__) == ……/webProject/test_case
    # os.path.join(os.path.dirname(__file__), "..") == ……/webProject/test_case/..
    # os.path.abspath(os.path.join(os.path.dirname(__file__), "..") == ……/webProject
    print("ini配置文件路径:", pathobj)
    return pathobj  # 返回了config.ini文件所在路径


def get_ini_date(sections, item):
    """关键字驱动
    :param sections: ini类型文件.sections
    :param item: get.item =>value
    :return: str
    """
    try:
        iniconf = path_ini()
        conf = configparser.ConfigParser()
        conf.read(iniconf, encoding="utf-8")
        print(conf.get(sections, item))
        return conf.get(sections, item)
    except Exception as error:
        print(format(error))


class SavePng(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_ini_date("Url", "baidu_url"))
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        print("This is end.")
        cls.driver.quit()

    def test_load_url(self):
        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_css_selector("#TANGRAM__PSP_10__footerULoginBtn").click()
        login_text = self.driver.find_element_by_class_name("pass-form-logo").text
        if login_text:
            usrname = input("请输入你的账号：")
            self.driver.find_element_by_id("TANGRAM__PSP_10__userName").send_keys(usrname)
        time.sleep(5)
        # self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
