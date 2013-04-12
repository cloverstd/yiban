# -*- coding: utf-8 -*-
# @Filename: friendship.py
# @Description: friendship API interface
# @Author: cloverstd
# @Blog: http://hui.lu

import json
import urllib2
from urllib import urlencode

def get_friend(access_token, uid, count=None, cursor=None):
    """
    获取指定用户好友列表
    :param access_token: access_token
    :param uid: 用户 id
    :param count: 可选，指定返回数
    :param cursor: 可选，游标
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/get_friend.json"
    data = dict(access_token=access_token,
            uid=uid)
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
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def get_follow(access_token, uid, count=None, cursor=None):
    """
    获取指定用户关注列表
    :param access_token: access_token
    :param uid: 用户 id
    :param count: 可选，指定返回数
    :param cursor: 可选，游标
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/get_follow.json"
    data = dict(access_token=access_token,
            uid=uid)
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
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def get_friend_in_common(access_token, fid, count=None, cursor=None):
    """
    @ERROR: 返回 40003 错误，缺少必须参数
    获取当前登录用户和指定用户的共同好友
    :param access_token: access_token
    :param fid: 用户 id
    :param count: 可选，指定返回数
    :param cursor: 可选，游标
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/get_friend_in_common.json"
    data = dict(access_token=access_token,
            fid=fid)
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
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def get_follow_in_common(access_token, fid, count=None, cursor=None):
    """
    @ERROR: 返回 40003 错误，缺少必须参数
    返回当前登录用户和指定用户的共同关注
    :param access_token: access_token
    :param fid: 用户 id
    :param count: 可选，指定返回数
    :param cursor: 可选，游标
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/get_follow_in_common.json"
    data = dict(access_token=access_token,
            fid=fid)
    if count:
        data.update(count=count)

    if cursor:
        data.update(cursor=cursor)

    # GET
    try:
        content = urllib2.urlopen("%s?%s" % (url, urlencode(data))).read()
        # print "%s?%s" % (url, urlencode(data))
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
        return None

    if "code" in content:
        result = json.loads(content.decode('gbk')) 
        return result['code']

    return json.loads(content)

def create(access_token, fid):
    """
    加关注操作
    :param access_token: access_token
    :param fid: 用户 id
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/create.json"
    data = dict(access_token=access_token,
            fid=fid)

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

def destroy(access_token, fid):
    """
    取消关注
    :param access_token: access_token
    :param fid: 用户 id
    :return: None 发生 HTTP Error 时，除非网络问题，一般都是 access_token 错误
             errcode int 错误代码
             正确返回 JSON 格式，
    """
    url = "https://api.yiban.cn/friendship/destroy.json"
    data = dict(access_token=access_token,
            fid=fid)

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
    access_token = "f150c7aacd13a0ef39988303c51fa16c82153e52"
    print destroy(access_token, 323618)
    # print get_friend(access_token, 684317)

