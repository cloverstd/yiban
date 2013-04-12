#易班开放平台 Python SDK#

- - - -


Python_SDK4yiban 是对易班 API 接口进行的一个简单封装，主要包括了 OAuth 的授权，和 API 接口的调用

目前已经完成了对已有的 API 接口的封装调用

具体查看[易班文档](http://open.yiban.cn/wiki/index.php?title=API文档)

##安装##
```
git clone 
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

###用户 users###
```
当前用户 API.user.me(access_token)
```
