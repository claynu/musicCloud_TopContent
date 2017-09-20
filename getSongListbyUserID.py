#-*-coding:utf-8-*-
import requests
import urllib


url = 'http://music.163.com/weapi/user/playlist?csrf_token='
headers = {
    'Host': 'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:55.0) Gecko/20100101 Firefox/55.0',
    'Accept': '/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Referer': 'http://music.163.com/user/home?id=359653823',
    'Content-Length': '484',
    'Cookie': 'JSESSIONID-WYYY=XtT1weAouu5375Ye2qYX%2BvoQjMFswai7pVFjUuZtXmDcsv6ZODcvB6i%5CziWpTQjtXgCuqyPo1GtMm44ao%2FAolR2o3BT7owKutKlhJ6bzO4uAgwj4onDmm%2FtITM7rrp1M%5Cku7Jm1FHppq%2BOM6wIQbCH9Mw0bljtbZxkedY5B%2BZFJwY%2BA%2F%3A1505229288826; _iuqxldmzr_=32; _ntes_nnid=fdeed19129ab51c709440b7ed9084c03,1505106792764; _ntes_nuid=fdeed19129ab51c709440b7ed9084c03; __utma=94650624.475475734.1505106794.1505188463.1505227489.7; __utmz=94650624.1505227489.7.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmb=94650624.4.10.1505227489; __utmc=94650624',
    'Connection': 'keep-alive',
}

data1 = {
    'params': 'yLZx7yKIWE16ew0zc1ltR1OGBf/mFE51T+hZMTLmXUzV+xVCupal7nVlh+tqCyrbXK6ayKQY482y0PQvRtSwj2B0H6Y1Y2bkiqp85A6NqOtWkp4cbSBtRQDkTxM1Wo3dEeD5wvR1QzW1UwEwas7Dsna0UESJwD/CutJpgV+hJKbDGx/B/AomSHy7Z6m+lTa1',
    'encSecKey': 'be1142de6b300e5c071f6ec7e102c395c016264785962f31203bb505ed478bad48ff41b52831e718302ea4b6dd35bbaf63b1bc7c4ed8139330075e8ef027def23fe9f19b49d15885140e8153ec292b658cff94a37dc5179e8500c10e3a00143a679064b15ef20edfeaf84673fa6c2c2607a76ffd50dda4e3fafd3ae8e446e26e',
}
data_post = urllib.urlencode(data1)
res = requests.post(headers=headers, url=url, data=data_post)
print res.content