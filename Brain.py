#!/usr/bin/env python
# encoding: utf-8

import numpy as np
#from decimal import Decimal

from Stock import StockPool

STOCK_KTYPE = 'D'
TIME_ZONE = ['2016-07-08', '2017-08-10']

class ThinkChange:
    '''up or down'''
    def __init__(self):
        self.idx = -1
        self.lastValue = 0
        self.featrue = np.ones((4,3), dtype=np.int)
        self.lastDecision = -1

    def makeDecide(self, price, decision=0):
        if decision > 0:
            self.idx = 2 if price > 0 else 3
        else:
            self.idx = 0 if price > 0 else 1

        self.lastDecision = decision
        deci = np.random.randint(0, self.featrue[self.idx][1])
        self.featrue[self.idx][0] += 1
        if deci <= self.featrue[self.idx][2]:
            self.featrue[self.idx][1] += 1
            return True
        return False

    def checkResult(self, price):
        if abs(self.lastValue) >0:
            if self.lastDecision > 0:
                wins = 0 if price >0 else 1
            else:
                wins = 0 if price <=0 else 1

            if self.idx >= 0:
                self.featrue[self.idx][2] += wins
        self.idx = -1



class Brain:
    def __init__(self):
        self.stock = StockPool()
        self.t_price = ThinkChange()
        self.t_volum = ThinkChange()

    def getStockInfo(self, code=None):
        self.code = self.stock.choiceRandomStock() if not code else code
        self.st_info = self.stock.getStockInfoDetail(self.code, STOCK_KTYPE, TIME_ZONE[0], TIME_ZONE[1])
        return np.array(self.st_info.sort_index())

    def makeDecide(self, st_info, decision = 0):
        price = self.t_price.lastValue - st_info[2] if self.t_price.lastValue>0 else st_info[2]
        volum = self.t_volum.lastValue - st_info[4] if self.t_volum.lastValue>0 else st_info[4]
        self.t_price.checkResult(price)
        self.t_volum.checkResult(price)
        ch_price = self.t_price.makeDecide(price, decision)
        ch_volum = self.t_volum.makeDecide(volum, decision)
        self.t_price.lastValue, self.t_volum.lastValue = st_info[2], st_info[4]
        print("p:%s v:%s" % (price, volum))
        return True if ch_price and ch_volum else False


if __name__ == "__main__":
    brain = Brain()
    brain.getStockInfo()
    print(brain.st_info.sort_index())
