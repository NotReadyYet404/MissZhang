from playsound import playsound
from youdao import YouDao
import random
import os
import requests
import re


def trans(english_word):

    url = 'https://fanyi.baidu.com/sug'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.190 Safari/537.36'
    }
    data = {
        'kw': english_word
    }
    responce = requests.post(url=url, data=data, headers=headers, timeout=1)

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
        with open('forget.md', 'r') as add_words:
            lines = add_words.readlines()   
            for line in lines:
                word = re.findall('[a-z]+', line)
                if word:
                    words.append(word[0])
        add_words.close()
        for index in range(0, len(words)):
            words[index] = words[index].replace('\n', '')
            yd.set_word(words[index])
            if yd.get_file_path():
                pass
            else:
                yd.download()
    file_object.close()
    with open("forget.md", 'w') as forget:
        forget.write('| CORRECT | TRANSLATION |\n')
        forget.write('|:-------:|:-----------:|\n')
        print('Finish initializing and enjoy by yourself ^_____^')
        i = 0
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
            i = i + 1
            print(i)
    forget.close()
