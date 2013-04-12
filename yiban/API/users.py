# -*- coding: utf-8 -*-
# @Filename: users.py
# @Description: user API interface
# @Author: cloverstd
# @Blog: http://hui.lu

import json
import urllib2
from urllib import urlencode

def me(access_token):
    """
    返回当前登录用户的基本信息
    :param access_token: access_token
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
    """
    url = "https://api.yiban.cn/users/me.json"
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

def real_me(access_token):
    """
    返回当前登录用户的真实信息
    :param access_token: access_token
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
    """
    url = "https://api.yiban.cn/users/real_me.json"
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

def get_show(access_token, uid):
    """
    返回指定用户的信息
    :param access_token: access_token
    :param uid: 用户 uid
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
    """
    url = "https://api.yiban.cn/users/get_show.json"
    data = dict(access_token=access_token, uid=uid)

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

def get_counts(access_token, uid):
    """
    返回指定用户的的好友数，粉丝数，微博数
    :param access_token: access_token
    :param uid: 用户 uid
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
    """
    url = "https://api.yiban.cn/users/get_counts.json"
    data = dict(access_token=access_token, uid=uid)

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

class YibanAPIException(Exception):
    def __init__(self, msg):
        self.error = msg

if __name__ == '__main__':
    access_token = ""
    # print get_me_infos(access_token)
    print get_me_real_info(access_token)
