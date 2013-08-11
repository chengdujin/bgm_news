#!/usr/bin/python
# -*- coding: utf-8 -*-

# @author Jin Yuan
# @contact jinyuan@baidu.com
# @created Jan 17, 2013

import sys
reload(sys)
sys.setdefaultencoding('UTF-8')

# SERVICES
from pymongo.connection import Connection
from pymongo.database import Database
from pymongo.collection import Collection
from pymongo.errors import CollectionInvalid
con = Connection('127.0.0.1:27017')
db = Database(con, 'news')

import redis
#rclient = redis.StrictRedis(host='10.240.35.40', port=6379)
rclient = redis.StrictRedis(host='127.0.0.1')


# CONSTANTS
PUBLIC = 'http://mobile-global.baidu.com/news/%s'
#LOCAL = '/home/work/STATIC/news/%s'
LOCAL = '/home/jinyuan/Downloads/news/%s'

TRANSCODED_LOCAL_DIR = LOCAL % 'ts/'
TRANSCODED_PUBLIC_DIR = PUBLIC % 'ts/'

IMAGES_LOCAL_DIR = LOCAL % 'img/'
IMAGES_PUBLIC_DIR = PUBLIC % 'img/'

MEDIA_LOCAL_DIR = LOCAL % 'mid/'
MEDIA_PUBLIC_DIR = PUBLIC % 'mid/'

NEWS_TEMPLATE = LOCAL % 'templates/index.html'
NEWS_TEMPLATE_ARABIC = LOCAL % 'templates/index_arabic.html'
UCK_TRANSCODING = 'http://gate.baidu.com/tc?m=8&from=bdpc_browser&src='
TRANSCODED_ENCODING = '<meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>\n'

TRANSCODING_BTN_EN = 'Original page'
TRANSCODING_BTN_PT = 'Página original'
TRANSCODING_BTN_JA = '元のページ'
TRANSCODING_BTN_IND = 'Laman Asli'
TRANSCODING_BTN_TH = 'หน้าเดิม'
TRANSCODING_BTN_AR = 'ﺎﻠﻤﺻﺩﺭ'
TRANSCODING_BTN_ZH_CN = '查看原始网页'
TRANSCODING_BTN_ZH_HK = '查看原始鏈接'

DATABASE_REMOVAL_DAYS = 90
MEMORY_RESTORATION_DAYS = 10
MEMORY_EXPIRATION_DAYS = 10

STRATEGY_WITHOUT_WEIGHTS = 1
STRATEGY_WITH_WEIGHTS = 2

FEED_REGISTRAR = 'feeds'
CATEGORY_REGISTRAR = 'categories'

PARAGRAPH_CRITERIA = 40
SUMMARY_LENGTH_LIMIT = 500
UCK_TIMEOUT = 3  # 3 seconds timeout

LANGUAGES = ['en', 'th', 'ind', 'ja', 'pt', 'en-rIN', 'ar', 'zh-CN', 'zh-HK']
MIN_IMAGE_SIZE = 150, 150
THUMBNAIL_STYLE = 1.4
THUMBNAIL_LANDSCAPE_SIZE = 451, 170
THUMBNAIL_PORTRAIT_SIZE = 176, 211
CATEGORY_IMAGE_SIZE = 189, 162
HOT_IMAGE_SIZE = 388, 162
