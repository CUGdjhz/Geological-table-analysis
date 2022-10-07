# -*-coding: utf-8 -*-
# @Time : 2022/4/27 10:55
# @Author : hewitt Wong
import os

import pycocotools.mask as mask
import json

from polis import PoLiS


class Format:
    def __init__(self):
        self._Dt_dir_path = None
        self.Dt = []
        self._Gt_file = None

    def load_file(self, file_path, model):
        if model == "DT":
            self._Dt_dir_path = file_path
        elif model == "GT":
            self._Gt_file = json.load(open(file_path, 'r', encoding='utf-8'))
        else:
            exit("Class:PoLiS Func:load_file: Model Error")

    def calculate(self, type):
        if 'J' == type:
            for idx in range(self._Gt_file['images'].__len__()):
                tmp_Dt_file_name = self._Gt_file['images'][idx]['file_name']
                Dt_file_path = ''.join(os.path.join(self._Dt_dir_path, tmp_Dt_file_name).split('.')[:-1]) + '.json'
                Dt_file = json.load(open(Dt_file_path))
                for i in range(Dt_file['object'].__len__()):
                    tmp_DT = {"category_id": 1, "image_id": self._Gt_file['images'][idx]['id'], 'score': 1}
                    tmp_arr = PoLiS.max_area(Dt_file['object'][i]['mask']).reshape((1, -1)).tolist()
                    h = self._Gt_file['images'][idx]["height"]
                    w = self._Gt_file['images'][idx]['width']
                    rle = mask.frPyObjects(tmp_arr, h, w)
                    rle[0]['counts'] = str(rle[0]['counts'], encoding='utf-8')
                    rle = rle[0]
                    tmp_DT["segmentation"] = rle
                    self.Dt.append(tmp_DT)

    def save(self, path):
        with open(path, 'w', encoding='utf-8') as json_file:
            json.dump(self.Dt, json_file, ensure_ascii=False)


def run(gt_path, dt_path, save_path, type):
    f = Format()
    f.load_file(gt_path, 'GT')
    f.load_file(dt_path, 'DT')
    f.calculate(type)
    f.save(save_path)


if __name__ == '__main__':
    run(r'H:\whtowerCode\PoLiS\datas\instances_test2014.json', r'H:\whtowerCode\PoLiS\datas\results_test_building',
        r"./datas/format.json", 'J')
