# -*- coding: utf-8 -*-
import urllib.request
import requests
from contextlib import closing
import time
import re
import os
import random
from lxml import html





# officialaccount_id = '695'
# article_id = '15233'
# sleeptime = 10
#
#
# def crawling():
#     # 登录session
#     session_requests = requests.session()
#     login_url = 'https://login.afreecatv.com/afreeca/login.php?szFrom=adult&request_uri=http%3A%2F%2Fvod.afreecatv.com%2FPLAYER%2FSTATION%2F57950624'
#     result = session_requests.post(
#         login_url,
#         data={
#             'Username': '1369269443',
#             'password': 'VaeVae2500',
#             'terminal': '1',
#             'InviteUserId': ''
#         },
#         headers=dict(referer=login_url)
#     )
#
#     body_message = result.content.decode('utf-8')
#     print(body_message)
#
# crawling()


def url_open(url):
    headers = {
        'Referer': 'http://vod.afreecatv.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req,timeout=5)
    html = response.read().decode('utf-8')
    return html

html = url_open('https://vod.afreecatv.com/PLAYER/STATION/56615918')
# print(html)
re.findall(r'http.*?',html)