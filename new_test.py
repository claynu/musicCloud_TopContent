import json
import base64
import rsa
from Crypto.Cipher import AES


text = {
    'username': '17608038113',
    'password': 'HY852521',
    'rememberLogin': 'true'
}
first_key = '0CoJUm6Qyw8W8jud'
vi = "0102030405060708"
text = json.dumps(text)
secKey = 16*'f'
text = base64.encode(AES.new(first_key, AES.MODE_CBC, vi).encrypt(text))
encText = base64.encode(AES.new(first_key, AES.MODE_CBC, vi).encrypt(text))

secKey = secKey[::-1]
rs = int(text.encode('hex'), 16) ** int('01001', 16) % int('00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7', 16)
encSecKey = format(rs, 'x').zfill(256)
data = {
    'params': encText,
    'encSecKey': encSecKey
}
print data
