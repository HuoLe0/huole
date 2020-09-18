import urllib.request
import re
import os,sys
import random
import time


def url_open(url):
    headers = {
        'Referer': 'https://jd.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html
def get_url(url):
    html = url_open(url).decode('utf-8')
    url1 = re.findall(r'//item.jd.com/.{1,100}.html',html)
    urls = []
    for i in url1:
        urls.append('https:' + str(i))
    return set(urls)

def get_img(each):
    html = url_open(url).decode('utf-8')
    photo1 = re.findall(r'//.*\.jpg', html)
    photos = []
    for i in photo1:
        photos.append('http:'+str(i))
    return set(photos)

def choose_url():
    print('输入数字（1~13）：\n1：校园风，2：性感，3：复古，4：优雅，5：轻奢旗袍风，6：职业风\n7：女仆风，8：可爱风，9：日式风，10：动漫风，11：夜店风，12：花嫁风，13：女王风')
    number = int(input('请输入要爬取的风格：\n'))

    urllist = ['https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_18036%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_35269%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_75548%5E&uc=0#J_searchWrap',
               'https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_76521%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_101110%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_114627%5E&uc=0#J_searchWrap',
               'https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125908%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125909%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125910%5E&uc=0#J_searchWrap',
               'https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125911%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125913%5E&uc=0#J_searchWrap','https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125914%5E&uc=0#J_searchWrap',
               'https://search.jd.com/search?keyword=%E6%83%85%E8%B6%A3%E5%86%85%E8%A1%A3&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&ds=1&suggest=1.his.0.0&psort=3&ev=872_125915%5E&uc=0#J_searchWrap']
    url = urllist[number-1]
    return url
url = choose_url()
urls = get_url(url)
folder = 'JD'
os.mkdir(folder)
os.chdir(folder)
count = 1
for each in urls:
    print(each)
    html1 = url_open(each).decode('utf-8')
    title = re.search(r'<title>.{1,100}</title>',html1)
    t1 = title.span()[0] + 7
    t2 = title.span()[1] -24
    #print(t1,t2)

    photos = get_img(each)
    for i in photos:
        print(i)
        mm = url_open(i)
        print('下载第'+str(count)+'张图片')
        with open(str(html1[t1:t2]) +str(count)+ '.jpg', 'wb') as f:
            f.write(mm)
            count += 1



