#!/usr/bin/env python
# encoding: utf-8

import tushare as tu, random

class StockPool:
    def __init__(self):
        self.st_list = tu.get_hs300s()

    def choiceRandomStock(self):
        _st = random.choice(self.st_list['code'].tolist())
        return _st

    def getStockInfo(self, code, ktype, start, end):
        _st_info = tu.get_k_data(code, ktype=ktype, start=start, end=end)
        return _st_info[['date', 'open', 'close', 'volume']]

    def getStockInfoDetail(self, code, ktype, start, end):
        _st_info = tu.get_hist_data(code, ktype=ktype, start=start, end=end)
        return _st_info


