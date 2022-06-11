import os
from tqdm import tqdm
from PIL import Image

dir_origin_path = "C:/Users/侯照坤/Desktop/python代码/deep_learning/fall-detection/yolov5-master/mydata/img1"
dir_save_path   = "C:/Users/侯照坤/Desktop/python代码/deep_learning/fall-detection/yolov5-master/mydata/img2"

img_names = os.listdir(dir_origin_path)
for img_name in tqdm(img_names):
    if img_name.lower().endswith(('.bmp', '.dib', '.png', '.jpg', '.jpeg', '.pbm', '.pgm', '.ppm', '.tif', '.tiff')):
        image_path  = os.path.join(dir_origin_path, img_name)
        image       = Image.open(image_path)
        image = image.convert('RGB')

        if not os.path.exists(dir_save_path):
            os.makedirs(dir_save_path)
        image.save(os.path.join(dir_save_path, img_name))
