# -*- coding: utf-8 -*-
# @Filename: register.py
# @Description: register API interface
# @Author: cloverstd
# @Blog: http://hui.lu

import json
import urllib2
from urllib import urlencode

def verify_nickname(access_token, nickname):
    """
    检查 nickname 是否被允许
    :param access_token: access_token
    :parm nickname: nickname
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
             此 JSON 中，允许则为1，不允许为空
    """
    url = "https://api.yiban.cn/register/verify_nickname.json"
    data = dict(access_token=access_token, nickname=nickname)

    # GET
    try:
        content = urllib2.urlopen("%s?%s" % (url, urlencode(data))).read()
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
        return None

    if "code" in content:
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def site_info(access_token):
    """
    获取所有学校基本信息
    :param access_token: access_token
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
             此 JSON 中，允许则为1，不允许为空
    """
    url = "https://api.yiban.cn/register/site_info.json"
    data = dict(access_token=access_token)

    # GET
    try:
        content = urllib2.urlopen("%s?%s" % (url, urlencode(data))).read()
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
        return None

    if "code" in content:
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

if __name__ == '__main__':
    access_token = ""
    print site_info(access_token)
