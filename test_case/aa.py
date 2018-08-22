import unittest
import os.path
import configparser
from selenium import webdriver


def get_init_data(content, key):
    """关键字驱动
    :param content: ini类型文件.sections
    :param key: get.item =>value
    :return: str
    """
    try:
        init_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))+"/Conf/config.ini"
        print(init_path)
        conf = configparser.ConfigParser()
        conf.read(init_path, encoding="utf-8")
        return conf.get(content, key)
    except Exception as err:
        print(err)


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.get(get_init_data("Url", "baidu_url"))
        cls.driver.implicitly_wait(10)
        print("This is begin")

    @classmethod
    def tearDownClass(cls):
        print("This is end.")
        cls.driver.quit()

    def test_equal_title(self):
        try:
            self.assertEqual("百度一下，你就知道", self.driver.title)
            print("assertEqual test pass.")
        except Exception as err:
            print("assertEqual test failed.", err)

    def test_in_title(self):
        try:
            self.assertEqual("百度一下，你就知道", self.driver.title)
            print("assertEqual test pass.")
        except Exception as err:
            print("assertEqual test failed.", err)


if __name__ == '__main__':
    unittest.main()
