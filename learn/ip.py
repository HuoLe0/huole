import urllib.request
import re

url = 'https://www.xicidaili.com/nt/'
req = urllib.request.Request(url)
req.add_header('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.162 Safari/537.36')
response = urllib.request.urlopen(req)

html = response.read().decode('utf-8')
#print(html)
idx = re.finditer(r'(([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])\.){3}([01]{0,1}\d{0,1}\d|2[0-4]\d|25[0-5])',str(html))

print([i.group() for i in idx])