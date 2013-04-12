# -*- coding: utf-8 -*-
# @Filename: notification.py
# @Description: notification API interface
# @Author: cloverstd
# @Blog: http://hui.lu

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
