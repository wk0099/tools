# -- coding:utf-8 --
import os


def Rename(path):
    file_name = os.listdir(path)
    for i, name in enumerate(file_name):
        old_path = path+'\\'+name
        if i < 10:
            i = '0' + str(i)
        new_path = path+'\\' + '00' + str(i) + '.jpg'
        os.renames(old_path, new_path)


path = './data'
Rename(path)
