import urllib.request
import re
import os,sys
import random
import time


def url_open(url):
    headers = {
        #'Referer': '',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html

def get_pages(each):
    html2 = url_open(each)
    t1 = re.search(r'<h2 class="entry_title">.{1,150}</h2>',html2)
    title = t1.group()[24:-6]
    ed2k1 = re.search(r'<p>.{0,3}链接.*?</p>',html2)
    ed2k2 = re.findall(r'<p>\d{0,2}.{1,30}<p>',html2)
    if ed2k1:
        ed2k = ed2k1.group()[3:-4]
    else:
        ed2k = ed2k2
    return title,ed2k
    #print(title)

urllist = ['https://www.fuli121.com/category/zhainanfuli']
url = random.choice(urllist)
html = url_open(url)
urls1 = re.findall(r'https://www.fuli121.com/.{1,10}.html.*?动态',html)
urls = []
for i in set(urls1):
    urls.append(i[0:34])
    # urls.append(i[0:34]+'/2')
    # urls.append(i[0:34] + '/3')
print(set(urls))

for each in set(urls):
    title,ed2k = get_pages(each)
    print(title)
    print(ed2k)

    folder = str(title)

    os.chdir('D:/python/learn')
    os.mkdir(folder)
    os.chdir(folder)
    count = 0
    html1_1 = url_open(each)
    urlsadd = re.findall(r'https://www.fuli121.com/.{1,10}\.html/\d',html1_1)
    s = []
    for j in set(urlsadd):
        s.append(str(url_open(j)))

    html1 = str(html1_1) + str(s)
    #print(s)
    # name = re.findall(r'<p>.{3,20}</p>', html1)
    # print('相关信息：')
    # for i in name:
    #     print(i[3:-4])
    # print(html1)

    img_addrs = re.findall(r'http://.{50,100}\.jpg',str(html1))
    gif_addrs = re.findall(r'http://.{50,100}\.gif',str(html1))
    addrs = set(img_addrs + gif_addrs)
    print(addrs)
    for each1 in set(addrs):

        headers = {
            #'Referer': 'https://www.fuli121.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
        }
        req = urllib.request.Request(each1, headers=headers)
        response = urllib.request.urlopen(req)
        mm_img = response.read()

        filename = str(count) + '.gif'

        print('下载第' + str(count) + '张图片')
        with open(filename, 'wb') as f:
            f.write(mm_img)
        file = open(title+'.txt','w')
        file.write(str(ed2k))
        count += 1



