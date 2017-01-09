# !/usr/bin/venv python3
# -*- coding: utf-8 -*-
import os
from PIL import Image
import argparse
import shutil
import imghdr

'''
格式化图片的脚本
脚本代码   文件路径  文件要格式化长宽
运行：python img.py "/Users/cyq/Desktop/imgs"  500
'''

parser = argparse.ArgumentParser()
parser.add_argument('filePath')
parser.add_argument('wh')
args = parser.parse_args()
savepath = args.filePath+"/" + 'resize'
if os.path.isdir(savepath):
    shutil.rmtree(savepath)
    os.mkdir(savepath)
else:
    os.mkdir(savepath)

for parent, dirnames, filenames in os.walk(args.filePath):
    for name in filenames:
        if parent == savepath:
            break
        f = os.path.join(parent, name)
        imgType = imghdr.what(f)
        if imgType == "jpeg" or imgType == "png":
            q, h = os.path.splitext(name)
            im = Image.open(f)
            w, h = im.size
            print(f, w, h, args.wh)
            if w > int(args.wh) or h > int(args.wh):
                im.thumbnail((int(args.wh), int(args.wh)))
                im.save(savepath+"/"+q+".jpg", 'jpeg')
            else:
                shutil.copy(f, savepath)







