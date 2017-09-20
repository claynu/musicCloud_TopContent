#-*-coding:utf-8-*-
import requests
import re
import urllib

import json
url = 'http://music.163.com/weapi/v1/resource/comments/R_SO_4_65528?csrf_token'
headers ={
        'Content-Type': 'application/x-www-form-urlencoded',
}

data1 = {
    'params': 'Wznvy7YsTHk58swambDd+v3IQO2Fl27XHuDWVQ9YE+SX98eDQobWbjznZdSCfKWruaNJMyA+y7'
              'Vq+r+oOuUspDL53DGpCVI1iGcPjZM0A4aNS6Ahe3WZm5L'
              'DCX+XD8fGnSbv6L2H3/WFVInI4GrMzJBJzj3Ipqqd9goOy+yk+s1sIqF3SaEaRv0BQanBAWld',
    'encSecKey': '2cba5e562572ef9b16cc15497fcd136efdf7322edd4bee5b14c'
                 '70f72ddd852b95f9d4f2dd68ca24170ce84969450abc7a28d607'
                 '446272f1905e039c0a749c833fc839ad07434a1ccc6ce53ac9385'
                 '0622f552f9da55e86051e227ad3495e8b0b7dd46a2272d03e3f06a3'
                 'e920c1c04828a4b91ac3a38eccb71497cc964869acb76',
}
data_post = urllib.urlencode(data1)
res = requests.post(headers=headers, url=url, data=data_post)
dict = (res.json())
print dict
json_content = json.loads(res.content)
print type(json_content['hotComments'])
for i in (json_content['hotComments']):
    print i['content']
print (json_content['comments'][19]['content'])
# print type(res.content) str