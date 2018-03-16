#!/usr/bin/env python
# encoding: utf-8

import numpy as np
import hashlib as hl
from var_dump import var_dump
#from decimal import Decimal

from Stock import StockPool

STOCK_KTYPE = 'W'
TIME_ZONE = ['2017-08-01', '2017-08-28']

C = 1.96

class Brain:
    def __init__(self):
        self.stock = StockPool()
        self.lastStInfo = None

    def getStockInfo(self, code=None):
        code = self.stock.choiceRandomStock() if not code else code
        st_info = self.stock.getStockInfo(code, STOCK_KTYPE, TIME_ZONE[0], TIME_ZONE[1])
        return np.array(st_info.sort_index()[['close', 'volume']])

    def checkFeature(self, st_info):
        if self.lastStInfo is not None:
            c_vol = st_info[1]/self.lastStInfo[1]
            c_pic = st_info[0] - self.lastStInfo[0]

        self.lastStInfo = st_info.copy()

    def makeDecide(self, st_info):
        if c_vol < 0.5 and c_pic < 0:
            return 'B'


if __name__ == "__main__":
    brain = Brain()
    st_info = brain.getStockInfo('600276')
    print(st_info)
