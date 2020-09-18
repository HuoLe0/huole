import urllib.request
import os
import random
import re

def url_open(url):

    headers = {
        'Referer': 'https://www.mzitu.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36'
    }
    req = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(req)
    html = response.read()
    return html

def find_images_url(url):
    html = url_open(url)
    images_url = re.findall(r'https://www.mzitu.com/\d\d\d\d\d\d', str(html))
    return images_url


def get_images_addrs(images_url):
    for each in set(images_url):

        html1 = url_open(each)
        images_addrs = re.findall(r'https://i3.mmzztt.com/\d\d\d\d/\d\d/\d\d[a-z]\d\d.jpg', str(html1))
    return images_addrs
        #print(idx1)


def save_images(folder,images_addrs):
    count = 1
    for each in set(images_addrs):
        for i in range(1, 50):
            if i < 10:
                img_addrs = each[0:-5] + str(i) + '.jpg'
            else:
                img_addrs = each[0:-6] + str(i) + '.jpg'

            mm_images = url_open(img_addrs)
            filename = img_addrs.split('/')[-1]
            print('下载第' + str(count) + '张图片')
            with open(filename, 'wb') as f:
                f.write(mm_images)
                count += 1

def download_mm(folder='SB'):

    os.mkdir(folder)
    os.chdir(folder)
    url = 'https://www.mzitu.com/'
    images_url = find_images_url(url)
    images_addrs = get_images_addrs(images_url)
    print(set(images_addrs))
    save_images(folder,images_addrs)


if __name__ == '__main__':
    download_mm()