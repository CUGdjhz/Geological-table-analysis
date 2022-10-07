#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
import time
from PIL import Image, ImageEnhance
from aip import AipOcr
import json

APP_ID = ''
API_KEY = ''
SECRET_KEY = ''
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

filename = 'ocr.json'
with open('sort.json', 'r', encoding='utf-8-sig', errors='ignore') as json_file:
    data = json.load(json_file, strict=False)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def image2text(fileName):
    image = get_file_content(fileName)
    dic_result = client.basicGeneral(image)
    res = dic_result['words_result']
    result = ''
    for m in res:
        result = result + str(m['words'])
    return result

def ocr(srcPath):
# 读取图片
    img_1 = Image.open(srcPath)
    for i in range(len(data)):
        crop_box = (int(data[i]['x1']), int(data[i]['y1']), int(data[i]['x2']), int(data[i]['y2'])) # 设置裁剪的位置
        img_2 = img_1.crop(crop_box)    # 裁剪图片
        img_2.save("./img-ocr/1.png")
        time.sleep(1)
        getresult = image2text("./img-ocr/1.png")
        print(getresult)
        data[i]['content'] = getresult


    data2 = json.dumps(data, indent=4, ensure_ascii=False)
    with open(filename, 'w') as f:
        f.write(data2)

ocr("./img/011.png")

# python裁剪图片并保存
#
# srcPath = "./img/02.png"
# dstPath = "./img-ocr/"



#img_2.save(dstPath)




# import aircv
# import pytesseract
# def matchImg(imgsrc, imgobj, confidence=0.2):
#  """
#   图片对比识别imgobj在imgsrc上的相对位置（批量识别统一图片中需要的部分）
#  :param imgsrc: 原始图片路径(str)
#  :param imgobj: 待查找图片路径（模板）(str)
#  :param confidence: 识别度（0<confidence<1.0）
#  :return: None or dict({'confidence': 相似度(float), 'rectangle': 原始图片上的矩形坐标(tuple), 'result': 中心坐标(tuple)})
#  """
#  imsrc = aircv.imread(imgsrc)
#  imobj = aircv.imread(imgobj)
#
#  match_result = aircv.find_template(imsrc, imobj,
#          confidence) # {'confidence': 0.5435812473297119, 'rectangle': ((394, 384), (394, 416), (450, 384), (450, 416)), 'result': (422.0, 400.0)}
#  if match_result is not None:
#   match_result['shape'] = (imsrc.shape[1], imsrc.shape[0]) # 0为高，1为宽
#
#  return match_result
#
#
#
# def cutImg(imgsrc, out_img_name, coordinate):
#  """
#   根据坐标位置剪切图片
#  :param imgsrc: 原始图片路径(str)
#  :param out_img_name: 剪切输出图片路径(str)
#  :param coordinate: 原始图片上的坐标(tuple) egg:(x, y, w, h) ---> x,y为矩形左上角坐标, w,h为右下角坐标
#  :return:
#  """
#  image = Image.open(imgsrc)
#  region = image.crop(coordinate)
#  region = ImageEnhance.Contrast(region).enhance(1.5)
#  region.save(out_img_name)
#
#  # !/usr/bin/python2.7
#  # -*- coding: utf-8 -*-
#
#  image = Image.open('img-ocr/1.png')
#  code = pytesseract.image_to_string(image)
#  print(code)
#
#
# cutImg("img/1.png", "img-ocr", (196, 80, 293, 605))