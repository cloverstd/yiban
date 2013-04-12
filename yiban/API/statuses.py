#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Filename: statuses.py
# @Description: statuses API interface
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

def get_public(access_token, counts=None):
    """
    获取最新公共微博
    :param access_token: access_token
    :param counts: 可选，返回微博数
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/statuses/get_public.json"
    data = dict(access_token=access_token)
    if counts:
        data.update(counts)

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

def get_show(access_token, id):
    """
    获取单条微博信息
    :param access_token: access_token
    :param id: 动态id
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/statuses/get_show.json"
    data = dict(access_token=access_token, id=id)

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

def get_topics(access_token, topic, count=None, cursor=None):
    """
    获取某一话题下的微博
    :param access_token: access_token
    :param topic: 话题
    :param count: 返回数
    :param cursor: 游标
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/statuses/get_topics.json"
    data = dict(access_token=access_token,
            topic=topic)

    if count:
        data.update(count=count)

    if cursor:
        data.update(cursor=cursor)

    # GET
    try:
        content = urllib2.urlopen("%s?%s" % (url, urlencode(data))).read()
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
        return None

    if "code" in content:
        print content.decode('gbk')
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def update(access_token, status, weiboid=None, pic=None, video=None):
    """
    发布一条动态信息
    :param access_token: access_token
    :param status: 微博
    :param weiboid: 139 说客 ID
    :param pic: 图片
    :param video: 视频地址
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/statuses/update.json"
    data = dict(access_token=access_token,
            status=status)

    if weiboid:
        data.update(weiboid=weiboid)
    if pic:
        data.update(pic=pic)
    if video:
        data.update(video=video)

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

def upload(access_token, status, pic):
    """
    上传一张图片
    :param access_token: access_token
    :param status: 微博
    :param pic: 图片地址
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/statuses/upload.json"
    data = dict(access_token=access_token,
            status=status,
            pic=pic)

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
    print update(access_token, "测试")
    print upload(access_token, "测试", "http://ww4.sinaimg.cn/bmiddle/94848de2jw1e3m258pkrfj.jpg")

