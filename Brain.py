#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import hashlib as hl
from var_dump import var_dump
#from decimal import Decimal

from Stock import StockPool

STOCK_KTYPE = 'D'
TIME_ZONE = ['2014-08-01', '2017-08-14']

C = 1.96

class Brain:
    def __init__(self):
        self.stock = StockPool()
        self.lastFeature = None
        self.lastStInfo = None
        self.features = {}

    def getStockInfo(self, code=None):
        code = self.stock.choiceRandomStock() if not code else code
        st_info = self.stock.getStockInfoDetail(code, STOCK_KTYPE, TIME_ZONE[0], TIME_ZONE[1])
        return np.array(st_info.sort_index()[['close', 'open', 'ma5', 'ma10', 'ma20', 'v_ma5', 'v_ma10', 'v_ma20', 'turnover']])

    def checkFeature(self, st_info):
        c_featrue = st_info.copy()
        if self.lastStInfo is not None:
            c_times = [1, 1, 0] if c_featrue[0] - self.lastStInfo[0] > 0 else [1, 0, 1]
            if self.lastFeature is not None:
                self.features[self.lastFeature] = self.features[self.lastFeature] + c_times if self.lastFeature in self.features else np.array(c_times)

            c_open  = c_featrue[1] - self.lastStInfo[0]
            c_featrue = c_featrue[1:] - self.lastStInfo[1:]
            c_featrue[0] = c_open
            self.lastFeature = hl.sha1((c_featrue > 0).tostring()).hexdigest()
        self.lastStInfo = st_info.copy()

    def makeDecide(self, st_info):
        if st_info.any():
            self.checkFeature(st_info)
            if self.lastFeature is not None:
                fea = self.features[self.lastFeature] if self.lastFeature in self.features else np.array([1, 0, 1])
                _win, _lose = fea[1]/fea[0], fea[2]/fea[0]
                _qa = _win / (1 if _lose == 0 else _lose)
                #print("win:%s, lose:%s, qa:%s" % (_win, _lose, _qa))
                if _qa < 1:
                    return 's'
                return 'w' if _qa < 2 else 'b'


if __name__ == "__main__":
    brain = Brain()
    st_info = brain.getStockInfo()
    for info in st_info:
        brain.makeDecide(info)
    print(brain.features)
    print(brain.stock.code)
