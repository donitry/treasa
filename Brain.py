#!/usr/bin/env python
# encoding: utf-8

import numpy as np
from decimal import Decimal

from Stock import StockPool
from Trade import Account

class Brain:
    def __init__(self, asset, prop, code, ktype):
        self.account = Account(asset, prop)
        self.stock = StockPool()
        if not code:
            code = self.stock.choiceRandomStock()
        self.st_info = self.stock.getStockInfo(code, ktype)



if __name__ == '__main__':
    brain = Brain(100000, 0.7, '600276', 'W')
    list = []
    stArr = np.array(brain.st_info[['open', 'close']])
    for s in stArr:
        rate = Decimal((s[1]-s[0])/s[0]).quantize(Decimal('0.0000'))
        close = Decimal(s[1]).quantize(Decimal('0.00'))
        list.append(float(rate))
        list.append(float(close))
    raArr = np.array(list,(brain.st_info.shape()))


    print(raArr)
