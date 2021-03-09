import requests


def trans(word):
    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    data = {
        'kw': word
    }
    responce = requests.post(url=url, data=data, headers=headers)

    obj = responce.json()
    # for a in obj['data']:
    #     print(a['v'])
    # print(obj['data'][0]['v'])
    return obj['data'][0]['v']
    # print(obj)
