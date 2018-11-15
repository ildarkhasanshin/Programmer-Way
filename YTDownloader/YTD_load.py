import os
import sys

import pytube
from pytube import YouTube
from func import downloadVideo

sys.getfilesystemencoding()
'UTF-8'


print('made by Irnil')
print('Программа "Качатель" с Ютуба. Прив, лол кек)')

path = os.getcwd()
print("Текущая директория: %s" % path)

while 1:
    try:
        key = int(input(" 1 чтобы скачать сюда,  2 скачать в другую папку, 3 чтобы выйти: \n"))
        if key != 1 and key != 2 and key != 3:
            key1 = int(input("Ошибка. Введите заново:"))

        if key == 1:

                    line = input("Введите адрес ролика")
                    rest, vidName = line.split('=')
                    downloadVideo(vidName)
                    break

        elif key == 2:

            while 1:
                try:
                    newDir = input('Введите адрес новой директории, куда скачать видео:')
                    os.chdir(newDir)
                except FileNotFoundError:
                    print('Путь указан неверно, либо не существует')

                else:
                    path = os.getcwd()
                    print("Текущая рабочая директория %s" % path)

                    line = input("Введите адрес ролика")
                    rest, vidName = line.split('=')
                    downloadVideo(vidName)
                    break

        elif key == 3:
            print('Пока!')
            break

        else:
            continue

        break
    except ValueError:
        print("Ошибка! Введите 1 или 2")

hold = input("Press Enter to exit")