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

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(get_init_data("Url", "baidu_url"))
        self.driver.implicitly_wait(10)  # 整个dirver生命周期隐式等待，无需多处设置
        print("This is begin")

    def tearDown(self):
        print("This is end.")
        self.driver.quit()

    def test_equal_title(self):
        try:
            self.assertEqual("百度一下,你就知道", self.driver.title)
            print("assertEqual test pass.")
        except Exception as err:
            print("assertEqual test failed.", err)
            raise err

    def test_in_title(self):
        try:
            self.assertIn("百度一下", self.driver.title)
            print("assertIn test pass.")
        except Exception as err:
            print("assertIn test failed.", err)


if __name__ == '__main__':
    unittest.main()
