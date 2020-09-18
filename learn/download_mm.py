
import urllib.request
import re
import os
from pathlib import Path
import time



os.mkdir('SB')
os.chdir('SB')

url = 'https://www.mzitu.com/'
headers = {
    'Referer': 'https://www.mzitu.com/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
}
req = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
idx = re.findall(r'https://www.mzitu.com/\d\d\d\d\d\d',str(html))
print('抓取到的页面为:',set(idx))
count = 0
for each in set(idx):
    headers = {
        'Referer': 'https://www.mzitu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }

    req1 = urllib.request.Request(each,headers=headers)
    response1 = urllib.request.urlopen(req1)
    html1 = response1.read().decode('utf-8')
    title_add1 = re.search(r'"main-title">',html1)
    title_add2 = re.search(r'</h2>', html1)
    #print(title_add1.span(),title_add2.span())
    title = html1[title_add1.span()[1]:title_add2.span()[0]]

    pages = re.findall(r'<span>\d\d</span>',html1)
    # print(pages)
    page = re.findall(r'\d\d',str(pages))
    # print(page)
    p = int(page[0])
    print('相册名称为：',title)
    print('共有'+str(p)+'张图片')
    idx1 = re.findall(r'https://i3.mmzztt.com/\d\d\d\d/\d\d/\d\d[a-z]\d\d.jpg',html1)
    print('本页首张图片地址为：',idx1)
    for each in set(idx1):
        for i in range(1,p):
            if i<10:
                img_addrs = each[0:-5] + str(i) + '.jpg'
            else:
                img_addrs = each[0:-6] + str(i) + '.jpg'

            count += 1
            headers = {
                'Referer': 'https://www.mzitu.com/',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
            }
            req2 = urllib.request.Request(img_addrs, headers=headers)
            response2 = urllib.request.urlopen(req2)
            mm_img = response2.read()
            filename = str(title) + img_addrs.split('/')[-1]
            print('下载第' + str(count) + '张图片')
            with open(filename, 'wb') as f:
                f.write(mm_img)
    count = 0