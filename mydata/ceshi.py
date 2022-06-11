import os
import numpy as np
import scipy.io as sio
import shutil
from lxml.etree import Element, SubElement, tostring
from xml.dom.minidom import parseString
import cv2

filename='000040.jpg'
img_path = 'C:/Software/datas/people/WiderPerson/Images/' + filename
print('Img :%s' % img_path)
img = cv2.imread(img_path)
width = img.shape[1]  # 获取图片尺寸
height = img.shape[0]  # 获取图片尺寸 360
print(width)
print(height)