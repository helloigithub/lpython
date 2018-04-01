import urllib.request
import urllib.parse
import json
import time

while True:
    content = input('请输入要翻译的内容(输入q!退出程序):')
    if content == 'q!':
        break
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'


    data = {}
    data['i'] = content
    data['from']='AUTO'
    data['to']='AUTO'
    data['smartresult']='dict'
    data['client']='fanyideskweb'
    data['salt']='1522513265792'
    data['sign']='b80352ac6ad3ddf1eba618f89ebe8bc3'
    data['doctype']='json'
    data['version']='2.1'
    data['keyfrom']='fanyi.web'
    data['action']='FY_BY_CLICKBUTTION'
    data['typoResult']='false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    req = urllib.request.Request(url, data, head)
    response = urllib.request.urlopen(url, data)

    html = response.read().decode('utf-8')


    target = json.loads(html)
    target = target['translateResult'][0][0]['tgt']

    print(target)

    time.sleep(5)
