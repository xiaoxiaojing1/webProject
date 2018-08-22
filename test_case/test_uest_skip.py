import unittest
from selenium import webdriver

debug = 10


class MyTestCase(unittest.TestCase):

    @classmethod  # 相当于java testNG里面的@BeforeClass
    def setUpClass(cls):
        print("执行MyTestCase")
        cls.driver = webdriver.Chrome()
        cls.driver.get("https://www.baidu.com")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("MyTestCase执行完毕")

    def test_one(self):  # assertIn
        url = "www.testerhome.com"
        self.assertIn("testhome", url, "{}里面不包含testhome".format(url))

    def test_assert_instance(self):  # assert被测对象的数据类型
        type1 = type(self.driver.title)
        self.assertIsInstance(self.driver.title, int, "测试对象是{}类型".format(type1))

    @unittest.skip("当前测试用例skip")  # 相当于java testNG里面的@Test(enabled = false)
    def test_something(self):
        print("skip")
        self.assertEqual(True, False)

    @unittest.skipIf(debug == 6, "skipIf：条件为ture，跳过")
    def test_skip_if(self):
        print("test_skip_if方法执行")

    @unittest.skipUnless(debug > 6, "skipUnless:条件为false，跳过")
    def test_skip_unless(self):
        print("test_skip_unless方法执行")


if __name__ == '__main__':
    unittest.main()


