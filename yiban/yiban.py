# -*- coding: utf-8 -*-
# @Author: cloverstd
# @Blog: http://hui.lu
# Copyright (c) <2013-04-11> <copyright cloverstd@gmail.com>
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

import json
import hmac
import hashlib
import urllib2
from urllib import urlencode
from base64 import standard_b64decode
from API import *

class YibanOAuth(object):
    """
    易班 OAuth 类
    """
    def __init__(self, app_key, app_secret, redirect_uri):
        self._app_key = app_key
        self._app_secret = app_secret
        self.redirect_uri = redirect_uri
        self.access_token = None
        self.refresh_token = None

    def parse_signed_request(self, signed_request):
        """
        解析站内应用传递来的 verify_request，并且验证用户是否授权

        :param signed_request: 站内应用传递来验证是否授权的值
        :return: None 当有错误发生，data 包含用户信息
        """
        encoded_sig, payload = signed_request.split(".")
        sig = standard_b64decode(encoded_sig)
        data = json.loads(standard_b64decode(payload))
        if data['algorithm'] != "HMAC-SHA256":
            return None
        expected_sig_hamc = hmac.new(self._app_secret, payload, hashlib.sha256)
        expected_sig = expected_sig_hamc.hexdigest()

        if sig != expected_sig:
            return None

        return data
    def get_OAuth_url(self, response_type="code"):
        """
        返回授权地址

        :param response_type: 授权类型，code 适用于站内应用，
                              token 适用于客户端应用
        :return: 授权地址
        """
        data = dict(
                client_id=self._app_key,
                redirect_uri=self.redirect_uri,
                response_type=response_type,
            )
        return "%s?%s" % (
                "https://graph.yiban.cn/authorize.php",
                urlencode(data),
                )

    def get_access_token(self, code, grant_type="code"):
        """
        获取 access_token 和 refresh_token
        :param code: 授权获取的 code，有效期 10 分钟，每次重新请求后都会失效
        :param grant_type: 站内应用为 "code"，客户端应用为 "token"

        :return: token 请求 access_token 返回的结果，None 发生错误时返回
        TODO: 客户端应用授权
        """
        data = dict(
                client_id=self._app_key,
                client_sercet=self._app_secret,
                grant_type="authorization_code",
                code=code,
                redirect_uri=self.redirect_uri,
                )

        url =  "%s?%s" % (
                "https://graph.yiban.cn/token.php",
                urlencode(data),
                )
        token = None
        try:
            token = json.loads(urllib2.urlopen(url).read())
        except urllib2.HTTPError, e:
            # print e.code
            if e.code == 400:
                print("code 已过期")
                return token

        if "error" in token.keys():
            raise YibanException("错误")

        self.access_token = token.get('access_token')
        self.refresh_token = token.get('refresh_token')

        return token

    def refresh_acess_token(self):
        """
        刷新 access_token

        :return: token 请求 access_token 返回的结果，None refresh_token 过期时返回
        """
        data = dict(
                client_id=self._app_key,
                grant_type="refresh_token",
                refresh_token=self.refresh_token,
                )
        url = "https://graph.yiban.cn/token.php"

        try:
            token = urllib2.urlopen(url, urlencode(data))
        except urllib2.HTTPError:
            print "refresh_token 过期"
            return None

        self.access_token = token.get('access_token')
        self.refresh_token = token.get('refresh_token')

        return token



class YibanException(Exception):
    def __init__(self, message):
        self.msg = message


if __name__ == '__main__':
    app_key = "cc6c4c20c140e0b470eeede0e79d79b0"
    app_secret = "c7e8fd3001ded3354f7552727111578e"
    yb = YibanOAuth(app_key, app_secret)
    # print yb.get_OAuth_url("http://apps.yiban.cn/genchapp")
    code = "9e72bd08119f2a17f5e6ece22570abf1530946fa"
    print yb.get_access_token(code, "http://apps.yiban.cn/genchapp")
