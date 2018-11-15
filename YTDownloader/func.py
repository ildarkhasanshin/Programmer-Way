import sys

import pytube
from pytube import YouTube
from pytube.exceptions import RegexMatchError

sys.getfilesystemencoding()
'UTF-8'


def downloadVideo(vidName):
    try:
        a = YouTube('https://www.youtube.com/watch?v=' + vidName)

    except NameError or RegexMatchError as e:
        print(e)
        print("Такого видео не существует или имя видео введено неверно.")

    else:
        print('Видео скачивается, пожалуйста ждите...')
        a.streams.first().download()
        print('Файл скачан.')