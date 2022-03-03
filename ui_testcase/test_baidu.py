import pytest
from selenium import webdriver
from time import sleep


class TestBaiDu:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()

    @classmethod
    def teardown_class(cls):
        print("退出")
        cls.driver.quit()

    def test_getbaidu(self):

        self.driver.get("https://www.baidu.com")
        sleep(2)

    def test_jd(self):
        self.driver.get("https://www.jd.com")
        sleep(2)
