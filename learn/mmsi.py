from you_get import common
import urllib.request
import urllib.parse
from urllib.parse import urlencode
import time
import re
import gzip
import json
from io import BytesIO


website = 'https://www.bilibili.com'
def url_open(url):
    headers = {
        'Referer': 'https://www.bilibili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req,timeout=5)
    html = response.read()
    buff = BytesIO(html)
    f = gzip.GzipFile(fileobj=buff)
    html = f.read().decode('utf-8')
    return html
def download(url,website):
    html = url_open(url)
    urls = re.findall(r'/video.*?\.videocard\.\d', html)
    # titles = re.findall(r'<h1 title=".*?"', html)
    # print(set(titles))
    # print(set(urls))
    for each in set(urls):
        url = website + each
        print(url)

        common.any_download(url, output_dir='D:/python/learn', merge=True)


url_search = 'https://search.bilibili.com/all?'
keywords = input('请输入搜索内容：')
key = {'keyword':keywords}
key_url = urlencode(key)
url_result = url_search + key_url
print(url_result)
headers = {
        'Referer': 'https://www.bilibili.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
req = urllib.request.Request(url_result, headers=headers)
response = urllib.request.urlopen(req,timeout=5)
html = response.read().decode('utf-8')
urls = re.findall(r'"//www\.bilibili\.com/video/.*?"',html)

print(set(urls))
for each in set(urls):
    url = 'https:' + each[1:-2]
    print('本页面地址为：',url)
    print('开始下载'+keywords)
    download(url,website)
