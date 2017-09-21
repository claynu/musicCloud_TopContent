import json
import base64
import rsa
from Crypto.Cipher import AES
import urllib
import requests

def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1]
    rs = int(text.encode('hex'), 16)**int(pubKey, 16)%int(modulus, 16)
    return format(rs, 'x').zfill(256)
def encrypto(text,key,vi):
    pad = 16-len(text)%16
    text +=pad * chr(pad)
    encryptor = AES.new(key,AES.MODE_CBC,vi)
    encText = encryptor.encrypt(text)
    encText = base64.b64encode(encText)
    print encText
    return encText

url = 'http://music.163.com/weapi/login/cellphone?csrf_token='

url = "http://music.163.com/weapi/v1/resource/comments/R_SO_4_30953009/?csrf_token="

headers = {
    'Cookie': 'appver=1.5.0.75771;',
    'Referer': 'http://music.163.com/'
}

text ={'username':'17608038113','password':'HY852521','rememberLogin':'true'}
text = json.dumps(text)

text ="{rid:\"\", offset:\"0\", total:\"true\", limit:\"20\", csrf_token:\"\"}"

first_key = '0CoJUm6Qyw8W8jud'
vi = "0102030405060708"
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
pubKey = '010001'
secKey = 16*'F'

#first encode
firencode = encrypto(text,first_key,vi)

#second encode

secEncode = encrypto(firencode,secKey,vi)
print secEncode
encSecKey = rsaEncrypt(secKey, pubKey, modulus)
data = {
    "params": secEncode,
    "encSecKey": '257348aecb5e556c066de214e531faadd1c55d814f9be95fd06d6bff9f4c7a41f831f6394d5a3fd2e3881736d94a02ca919d952872e7d0a50ebfa1769a7a62d512f5f1ca21aec60bc3819a9c3ffca5eca9a0dba6d6f7249b06f5965ecfff3695b54e1c28f3f624750ed39e7de08fc8493242e26dbc4484a01c76f739e135637c'
}
print 'params='+data["params"]+'&encSecKey='+data["encSecKey"]
response = requests.post(url, headers=headers, data=data)
print response.content
res = requests.post(url, headers=headers, data=data)
if res.content!='':
    res_json = json.loads(res.content)
    for i in  res_json['comments']:
        print i['content']