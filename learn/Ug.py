import urllib.request
import os
import re
import random

def url_open(url):
    headers = {
        'Referer': 'https://www.meitulu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read().decode('utf-8')
    return html


def get_album(url):
    html = url_open(url)
    album1 = re.findall(r'https://www.meitulu.com/item/\d{1,5}.html', html)
    album = set(album1)
    #print(album)
    return album

def get_img_addrs(each,pages):
    html1 = url_open(each)
    img_1 = set(re.findall(r'https://mtl.gzhuibei.com/images/img/\d{1,5}/1.jpg', html1))
    #print(str(img_1)[2:-7])
    img_addrs = []
    for i in range(1,pages):
        addrs = str(img_1)[2:-7] + str(i) + '.jpg'
        img_addrs.append(addrs)
    #print(img_addrs)
    return img_addrs

def find_pages(each):
    html1 = url_open(each)
    title_add1 = re.search(r'<h1>', html1)
    title_add2 = re.search(r'</h1>', html1)
    # print(title_add1.span(),title_add2.span())
    title = html1[title_add1.span()[1]:title_add2.span()[0]]
    p = re.findall(r'图片数量： \d\d 张', html1)
    print(title,p)
    page = re.findall(r'\d\d', str(p))
    #print(page)
    page.append('1')
    pages = int(max(page))
    return pages,title


urllist = ['https://www.meitulu.com/','https://www.meitulu.com/t/yingsihui-wings/','https://www.meitulu.com/t/bomb.tv/','https://www.meitulu.com/t/wpb-net/',
           'https://www.meitulu.com/t/qingdouke/','https://www.meitulu.com/t/tuigirl/','https://www.meitulu.com/t/xiuren/','https://www.meitulu.com/t/1371/',
           'https://www.meitulu.com/t/imiss/','https://www.meitulu.com/t/dianannan/','https://www.meitulu.com/t/youwuguan/','https://www.meitulu.com/t/yunvlang/']
url = random.choice(urllist)
path = 'D:\python\learn'

album = get_album(url)
for each in album:

    count = 1
    pages,title = find_pages(each)
    folder = title
    
    os.chdir('D:\python\learn')
    os.mkdir(folder)
    os.chdir(folder)
    img_addrs = get_img_addrs(each,pages)
    for each1 in img_addrs:
        headers = {
            'Referer': 'https://www.meitulu.com/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
        }
        req2 = urllib.request.Request(each1, headers=headers)
        response2 = urllib.request.urlopen(req2)
        mm_img = response2.read()

        filename = str(count)+'.jpg'
        print('下载第' + str(count) + '张图片')
        with open(filename, 'wb') as f:
            f.write(mm_img)
            count += 1
