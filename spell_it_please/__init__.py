from playsound import playsound
from youdao import YouDao
import random
import os
import requests


def trans(english_word):

    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    data = {
        'kw': english_word
    }
    responce = requests.post(url=url, data=data, headers=headers)

    obj = responce.json()
    # for a in obj['data']:
    #     print(a['v'])
    # print(obj['data'][0]['v'])
    return obj['data'][0]['v']
    # print(obj)


if __name__ == '__main__':
    print('Initializing....')
    yd = YouDao()
    with open('source.txt') as file_object:
        words = (file_object.readlines())
        for index in range(0, len(words)):
            words[index] = words[index].replace('\n', '')
            yd.set_word(words[index])
            if yd.get_file_path():
                pass
            else:
                yd.download()
    file_object.close()
    with open("forget.md", 'a') as forget:
        print('Finish initializing and enjoy by yourself ^_____^')
        while len(words) != 0:
            index = random.randint(0, len(words) - 1)
            path = os.path.join(yd.get_dir(), words[index] + '.mp3')
            try:
                playsound(path)
            except UnicodeError:
                del words[index]
                continue
            word = input("If you forget, just 'x': ")
            if word == words[index]:
                pass
            elif word == 'x':
                continue
            else:
                forget.write('|' + words[index] + '|' + trans(words[index]) + '|\n')
            del words[index]
    forget.close()
#     playsound('victory.mp3')
