#易班开放平台 Python SDK#

- - - -


Python_SDK4yiban 是对易班 API 接口进行的一个简单封装，主要包括了 OAuth 的授权，和 API 接口的调用

目前已经完成了对已有的 API 接口的封装调用

具体查看[易班文档](http://open.yiban.cn/wiki/index.php?title=API文档)

##安装##
```
git://github.com/cloverstd/yiban.git
```

##使用说明##
```
from yiban import YibanOAuth

APP_KEY = "your app key"
APP_SECRET = "your app secret"

yb = YibanOAuth(APP_KEY, APP_SECRET, your_redirect_uri)

# 站内应用处理 POST 过来的 verify_request
result = yb.parse_signed_request(verify_request)

# 引导用户授权
print yb.get_OAuth_url()
code = raw_input("Enter the verification code: ")
token = get_access_token(code)
```

##接口说明##

所有返回数据以易班官方文档为准

```
from yiban import API
```

###用户 users###
```
当前用户信息 API.user.me(access_token)
当前用户真实信息 API.user.real_me(access_token)
指定用户信息 API.user.get_show(access_token, uid)
指定用户的好友数，粉丝数，微博数 API.user.get_counts(access_token, uid)
```

###动态 statuses###
```
最新公共微博 API.statuses.get_public(access_token, counts)
单条微博 API.statuses.get_show(access_token, id)
某一话题下的微博 API.statuses.get_topics(access_token, topic, count, cursor)
发微博 API.statuses.update(access_token, status, weiboid, pic, video)
上传照片 API.statuses.upload(access_token, status, pic)
```

###关系 friendship###
```
指定用户好友列表 API.friendship.get_friend(access_token, uid, count, cursor)
指定用户关注列表 API.friendship.get_follow(access_token, uid, count, cursor)
当前用户和指定用户的共同好友 API.friendship.get_friend_in_common(access_token, fid, count, cursor) # 错误发生，40003
当前用户和指定用户的共同关注 API.friendship.get_follow_in_common(access_token, fid, count, cursor) # 错误发生，40003
```

###注册 register###
```
检查昵称是否允许 API.register.verify_nickname(access_token, nickname)
所有学校信息 API.site_info(access_token)
```

###消息 notification###
```
发送站内信 API.notification.send_site_mail(access_token, uid, content)  # 高级接口
发送系统消息 API.notification.send_sys_message(access_token, content, uid) # 高级接口
```

Changelog

v0.0.1 [2013-04-11]
