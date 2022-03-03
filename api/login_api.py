from api import base_url
import requests

from tools.get_log import GetLog

logger = GetLog.get_logger()


class LoginApi:
    # 1.初始化url
    def __init__(self):
        self.login_url = base_url + "/api/sys/login"
        logger.info("初始化登录接口:{}".format(self.login_url))

    def login_api(self, mobile, password):
        logger.info("正在请求登录接口:{}".format(self.login_url))
        data = {
            "Content-Type ": "application/json",
            "mobile": mobile,
            "password": password
        }
        return requests.post(self.login_url, json=data)
