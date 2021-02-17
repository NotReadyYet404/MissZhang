from playsound import playsound
from youdao import YouDao
import random
import os


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
with open("forget.md", 'w') as forget:
    forget.write('|   CORRECT  |   MY    |\n')
    forget.write('|:----------:|:-------:|\n')
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
            forget.write('|' + words[index] + '|' + word + '|\n')
        del words[index]

playsound('victory.mp3')
