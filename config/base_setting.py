# coding: utf-8
SERVER_PORT = 80
DEBUG = False
SQLALCHEMY_ECHO = False

JSON_AS_ASCII = False
AUTH_COOKIE_NAME="mooc_food"

SEO_TITLE = "Python Flask构建微信小程序订餐系统"

PAGE_SIZE=5
PAGE_DISPLAY=3

##过滤url
IGNORE_URLS=[
    "^/user/login",
    "^/api"
]

IGNORE_CHECK_LOGIN_URLS=[
    "^/static",
    "^/favicon.ico"
]

STATUS_MAPPING={
    "1":"正常",
    "0":"已删除"
}

MINA_APP={
    "appid":"wxde9227f5ddae43c1",
    "appkey":"271a97507281da80c502d7a4c31c657c",
    'paykey':'',
    'mch_id':'',
    'callback_url':'/api/order/callback'
}

UPLOAD = {
    'ext':[ 'jpg','gif','bmp','jpeg','png' ],
    'prefix_path':'/web/static/upload/',
    'prefix_url':'/static/upload/'
}

APP = {
    'domain':'http://dec.com:80'
}

API_IGNORE_URLS = [
    "^/api"
]

PAY_STATUS_MAPPING = {
    "1":"已支付",
    "-8":"待支付",
    "0":"已关闭"
}

PAY_STATUS_DISPLAY_MAPPING = {
    "0":"订单关闭",
    "1":"支付成功",
    "-8":"待支付",
    "-7":"待发货",
    "-6":"待确认",
    "-5":"待评价"
}