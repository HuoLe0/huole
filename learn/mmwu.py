# -*- coding: utf-8 -*-
import urllib.request
import requests
from contextlib import closing
import time
import re
import os
import random

def url_open(url):
    headers = {
        'Referer': 'https://www.mmwu.cc/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req,timeout=5)
    html = response.read()
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

o_urllist = ['https://www.mmwu.cc/tags-21.html','https://www.mmwu.cc/tags-2.html','https://www.mmwu.cc/tags-51.html',
             'https://www.mmwu.cc/']
o_url = random.choice(o_urllist)
o_html = url_open(o_url).decode('utf-8')
o_urls = re.findall(r'https://www\.mmwu\.cc/post/.*?\.html',o_html)
print(o_urls)
for url in set(o_urls):
    # url = random.choice(o_urls)
    html = url_open(url).decode('utf-8')
    title = re.search(r'<title>.*?</title>', html)
    # print(html)
    print(title.group()[7:-9])
    m3u8 = re.findall(r'https.*?\.m3u8', html)
    print(m3u8)
    count = 1
    folder = str(title.group()[7:-9])
    for each in m3u8:
        os.chdir('D:/python/learn')
        os.mkdir(folder)
        os.chdir(folder)
        m3u8_1 = each
        heads = re.search(r'https://www.19jvideo.com/.{1,30}/', m3u8_1)
        # print(heads.group())
        print('第一层m3u8链接：', m3u8_1)
        m = requests.get(m3u8_1)
        m.raise_for_status()
        text = m.text
        ts = re.findall(r'.*?\.ts', text)
        print(ts)
        for i in ts:
            addrs = heads.group() + i
            mm_video = url_open(addrs)
            print('开始下载第' + str(count) + '个文件')
            with open(str(i).replace('.ts', '') + '.ts', 'wb') as f:
                f.write(mm_video)

            print('第' + str(count) + '个文件下载完成')
            count += 1
        print("开始合并...")
        root = 'D:/python/learn/' + folder
        outdir = "output"
        os.chdir(root)
        if not os.path.exists(outdir):
            os.mkdir(outdir)
        os.system("copy /b *.ts " + str(count) + ".mp4")
        os.system("move " + str(count) + ".mp4" + " {}".format(outdir))
        print("结束合并...")




