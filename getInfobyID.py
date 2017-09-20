#-*-coding:utf-8-*-
#get song`s info and singer info from song`s id
import requests
import json

headers = {

    }
id = '1940312'
url = 'http://music.163.com/api/song/detail/?id='+id+'&ids=['+id+']'
# url = 'http://music.163.com/api/song/detail/?id=5250048&ids=[5250048]'  #url原型
res = requests.get(url = url,headers = headers)
json_songs = (json.loads(res.content))

print json_songs['songs'][0]['name'], #歌曲名
print '--'+json_songs['songs'][0]['artists'][0]['name'] #歌手
print json_songs['songs'][0]['artists'][0]['id'] #歌手id
print json_songs['songs'][0]['artists'][0]['picUrl']
print json_songs['songs'][0]['artists'][0]['img1v1Url']