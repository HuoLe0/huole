# -*- coding: utf-8 -*-
import urllib.request
import requests
from contextlib import closing
import time
import re
import os

def url_open(url):
    headers = {
        'Referer': 'https://www.yy3t.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def download_file(url, path,):

    with closing(requests.get(url, stream=True)) as r:
        chunk_size = 1024 * 10
        content_size = int(r.headers['content-length'])
        print('下载开始')
        with open(url.split('/')[-1]+'.ts', "wb") as f:
            p = ProgressData(size=content_size, unit='Kb', block=chunk_size)
            for chunk in r.iter_content(chunk_size=chunk_size):
                f.write(chunk)
                p.output()



class ProgressData(object):

    def __init__(self, block, size, unit, file_name='', ):
        self.file_name = file_name
        self.block = block / 1000.0
        self.size = size / 1000.0
        self.unit = unit
        self.count = 0
        self.start = time.time()

    def output(self):
        self.end = time.time()
        self.count += 1
        speed = self.block / (self.end - self.start) if (self.end - self.start) > 0 else 0
        self.start = time.time()
        loaded = self.count * self.block
        progress = round(loaded / self.size, 4)
        if loaded >= self.size:
            print(u'%s下载完成\r\n' % self.file_name)
        else:
            time.sleep(2)
            print(u'{0}下载进度{1:.2f}{2}/{3:.2f}{4} 下载速度{5:.2%} {6:.2f}{7}/s'. \
                format(self.file_name, loaded, self.unit, \
                       self.size, self.unit, progress, speed, self.unit))
            #print('%50s' % ('/' * int((1 - progress) * 50)))

# url = 'http://www.yongjiuzy1.com/?m=vod-type-id-21.html'
# html = url_open(url)
# v1 = re.findall(r'/\?m=vod-detail-.{1,5}-.{1,8}.html',html)
# v2 = []
# for each in v1:
#     urls = 'http://www.yongjiuzy1.com/' + str(each)
#     v2.append(urls)
# #print(v2)
# for each in v2:
#
#     html1 = url_open(urls)
#     video_url = re.findall(r'https://.{1,50}.com/.{1,20}/.{1,100}',html1)
#     print(set(video_url))
url='https://www.yy3t.com/play/25382-1-1/'
html = url_open(url)
title = re.search(r'<title>.*?</title>',html)
print(title.group()[7:-24])
m3u8 = re.findall(r'https.*?\.m3u8',html)
count = 1
folder = str(title.group()[7:-24])
for each in m3u8:
    os.chdir('D:/python/learn')
    os.mkdir(folder)
    os.chdir(folder)
    m3u8_1 = str(each).replace('\\','')
    print('第一层m3u8链接：', m3u8_1)
    m = requests.get(m3u8_1)
    m.raise_for_status()
    text = m.text
    idx = re.findall(r'\n.*?\.m3u8',text)
    key = idx[0][1:]
    #print(key)
    idx = re.search(r'/index\.m3u8',m3u8_1)
    m3u8_2 = m3u8_1[:int(idx.span()[0])+1]+key
    print('第二层m3u8链接：', m3u8_2)
    html1 = url_open(m3u8_2)
    ts = re.findall(r'.*?\.ts',html1)
    print('获取的ts文件为：',ts)
    heads = m3u8_2.replace(idx.group(),'/')
    #print(heads)
    for i in ts:
        addrs = heads + i
        print('下载第'+str(count)+'个文件')
        download_file(addrs,path='D:/python/learn')
        count += 1
    print("开始合并...")
    root = folder
    outdir = "output"
    os.chdir(root)
    if not os.path.exists(outdir):
        os.mkdir(outdir)
    os.system("copy /b *.ts new.mp4")
    os.system("move new.mp4 {}".format(outdir))
    print("结束合并...")






