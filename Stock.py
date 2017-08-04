#!/usr/bin/env python
# encoding: utf-8

import tushare as tu, random

class StockPool:
    def __init__(self):
        self.st_list = tu.get_sz50s()

    def choiceRandomStock(self):
        _st = random.choice(self.st_list['code'].tolist())
        return _st

    def getStockInfo(self, code, ktype, start):
        _st_info = tu.get_k_data(code, ktype=ktype, start=start)
        return _st_info[['open', 'close', 'volume']]

