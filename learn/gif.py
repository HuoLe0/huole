import urllib.request
import re
import os,sys
import random
import time


def url_open(url):
    headers = {
        'Referer': 'http://bbbt.net/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_pages(each):
    html2 = url_open(each)
    t1 = re.search(r'<title>.{1,30}</title>',html2)
    title = t1.group()[7:-8]

    return title
    #print(title)

urllist = ['http://bbbt.net/tag/gif%E5%87%BA%E5%A4%84','http://bbbt.net/tag/%E7%A6%8F%E5%88%A9%E5%90%A7']
url = random.choice(urllist)
html = url_open(url)
urls = re.findall(r'http://bbbt.net/.{1,8}.html',html)
#print(set(urls))

for each in set(urls):
    title = get_pages(each)
    folder = str(title)

    os.chdir('D:/python/learn')
    os.mkdir(folder)
    os.chdir(folder)
    count = 1
    html1 = url_open(each)
    name = re.findall(r'<p>.{3,20}</p>', html1)
    print('相关信息：')
    for i in name:
        print(i[3:-4])
    #print(html1)
    img_addrs = re.findall(r'https://tva1.sinaimg.cn/.{1,7}/.{10,80}.gif',str(html1))
    #print(set(img_addrs))
    for each1 in set(img_addrs):

        headers = {
            'Referer': 'http://bbbt.net/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
        }
        req = urllib.request.Request(each1, headers=headers)
        response = urllib.request.urlopen(req)
        mm_img = response.read()

        filename = str(count) + '.gif'
        print('下载第' + str(count) + '张图片')
        with open(filename, 'wb') as f:
            f.write(mm_img)
            count += 1



