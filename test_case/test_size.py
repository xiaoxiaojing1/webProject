from selenium import webdriver
import configparser
import os


def get_init_data(section, key):
    """关键字驱动
    :param section: ini类型文件.sections
    :param key: get.key =>value
    :return: str
    """
    try:
        project_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        init_path = project_path + "/Conf/config.ini"
        print("ini文件地址为：", init_path)
        conf = configparser.ConfigParser()
        conf.read(init_path, encoding="utf-8")
        return conf.get(section, key)
    except Exception as err:
        print(err)


class Login(object):

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get(get_init_data("Url", "baidu_url"))
        self.driver.implicitly_wait(10)

    def test_size(self):
        obj = self.driver.page_source.__sizeof__()
        print("网页尺寸为{}kb".format(int(obj / 1024)))
        self.driver.quit()


testsize = Login()
testsize.test_size()
