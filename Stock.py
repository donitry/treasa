#!/usr/bin/env python
# encoding: utf-8

import tushare as tu, numpy as np, pandas as pd, random

class StockPool:
    def __init__(self):
        self.st_list = tu.get_sz50s()

    def choiceRandomStock(self):
        _st = random.choice(self.st_list['code'].tolist())
        return _st

    def getStockInfo(self, code):
        _st_info = tu.get_k_data(code)
        return _st_info[['close', 'volume']]


if __name__ == '__main__':
    _cst = StockPool()
    code = _cst.choiceRandomStock()
    print(_cst.getStockInfo(code))

