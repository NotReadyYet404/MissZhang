import os
import requests
import re
import time


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
    return obj['data'][0]['v']

if __name__ == "__main__":
    with open('unsplited.md', 'r') as file_object:
        words = []
        num = 0
        lines = file_object.readlines()
        with open('splitBy20.md', 'w') as want:
            for line in lines:
                word = re.findall('[a-z]+', line)
                if len(word) == 0:
                    continue
                chinese = trans(word)
                time.sleep(1)
                if num % 20 == 0:
                    want.write('\n| Group ' + str(int(num / 20) + 1) + ' ||\n')
                    want.write('|:-----:|:---:|\n')
                want.write('| ' + word[0] + ' | ' + chinese + ' |\n')
                num += 1
