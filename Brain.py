#!/usr/bin/env python
# encoding: utf-8

import numpy as np
#from decimal import Decimal

from Stock import StockPool

STOCK_KTYPE = 'D'
TIME_ZONE = ['2017-07-10', '2017-08-10']

class Brain:
    def __init__(self, code):
        self.stock = StockPool()
        self.code = self.stock.choiceRandomStock() if not code else code
        self.st_info = self.stock.getStockInfoDetail(self.code, STOCK_KTYPE, TIME_ZONE[0], TIME_ZONE[1])

    class StockPrice:
        def __init__(self):
            self.tolTests = 0
            self.featrue = np.zeros((2,3), dtype=np.int)


    def test(self):
        t1 = self.StockPrice()
        print(t1.featrue)


if __name__ == "__main__":
    brain = Brain(None)
    print(brain.test())
