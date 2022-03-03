import logging

import pytest

from api.login_api import LoginApi
from tools.get_log import GetLog
from tools.read_yaml import read_yaml_data


class TestLogin:
    def setup_class(self):
        self.logger = GetLog.get_logger()
        self.login = LoginApi()

    def teardown_class(self):
        pass

    @pytest.mark.parametrize("mobile, password,expect", read_yaml_data("login.yaml"))
    def test_001(self, mobile, password, expect):
        """
        登录测试用例
        :param mobile: 用户名
        :param password: 密码
        :param expect: 预期结果，用于断言
        """
        print("传入参数结果为mobile：{}，password:{}".format(mobile, password))
        response = self.login.login_api(mobile, password)
        try:
            assert expect == response.json().get("code")
            self.logger.info("断言成功，响应结果为：{}".format(response.json()))
            print("响应结果为：", response.json())
        except Exception as e:
            self.logger.error("断言出错：{}".format(e))
            raise


if __name__ == '__main__':
    pytest.main(['-vs'])
