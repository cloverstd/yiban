#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: notification.py
# @Description: notification API interface
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
import urllib2
from urllib import urlencode

def send_site_mail(access_token, uid, content):
    """
    发送站内信（高级接口）
    :param access_token: access_token
    :param uid: 用户 id
    :param content: 内容（小于 180 汉字）
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
             此 JSON 中，允许则为1，不允许为空
    """
    url = "https://api.yiban.cn/notification/send_site_mail.json"
    data = dict(access_token=access_token,
                uid=uid,
                content=content)

    # POST
    try:
        content = urllib2.urlopen(url, urlencode(data)).read()
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
        return None

    if "code" in content:
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def send_sys_message(access_token, content, uid=None):
    """
    发送系统消息（高级接口）
    :param access_token: access_token
    :param uid: 可选，用户 id
    :param content: 内容（小于 180 汉字）
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式
             此 JSON 中，允许则为1，不允许为空
    """
    url = "https://api.yiban.cn/notification/send_site_mail.json"
    data = dict(access_token=access_token,
                content=content)
    if uid:
        data.update(uid=uid)

    # POST
    try:
        content = urllib2.urlopen(url, urlencode(data)).read()
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
