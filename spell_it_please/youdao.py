import os
import urllib.request


class YouDao():
    def __init__(self, type=0, word='hellow'):
        word = word.lower()
        self._type = type
        self._word = word

        # file root
        self._dirRoot = os.path.dirname(os.path.abspath(__file__))
        if 0 == self._type:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')  # 美音库
        else:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')  # 英音库

        if not os.path.exists('Speech_US'):
            os.makedirs('Speech_US')
        if not os.path.exists('Speech_EN'):
            os.makedirs('Speech_EN')

    def set_word(self, word):
        self._word = word

    def set_accent(self, type=0):
        self._type = type

        if 0 == self._type:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_US')  # 美音库
        else:
            self._dirSpeech = os.path.join(self._dirRoot, 'Speech_EN')  # 英音库

    def get_dir(self):
        return self._dirSpeech

    def get_accent(self):
        return self._type

    def download(self):
        self._word = self._word.lower()
        tmp = self.get_file_path()
        if tmp is None:
            self.set_url()
            try:
                urllib.request.urlretrieve(self._url, filename=self._filePath)
                return True
            except Exception:
                print('Warning: cannot download: ' + self._word)
                return False

        return self._filePath

    def set_url(self):
        # It's a private function to get the youDao url:
        # http://dict.youdao.com/dictvoice?type=0&audio=
        self._url = r'http://dict.youdao.com/dictvoice?type=' + str(
            self._type) + r'&audio=' + self._word

    def get_file_path(self):
        self._fileName = self._word + '.mp3'
        self._filePath = os.path.join(self._dirSpeech, self._fileName)

        if os.path.exists(self._filePath):
            return self._filePath
        else:
            return None
