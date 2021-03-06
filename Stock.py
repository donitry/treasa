#!/usr/bin/env python
# encoding: utf-8

import tushare as tu, random

class StockPool:
    def __init__(self, st_list=None):
        self.code = None
        self.st_list = tu.get_hs300s() if not st_list else st_list

    def choiceRandomStock(self):
        self.code = random.choice(self.st_list['code'].tolist())
        return self.code

    def getStockInfo(self, code, ktype, start, end):
        _st_info = tu.get_k_data(code, ktype=ktype, start=start, end=end)
        return _st_info[['date', 'open', 'close', 'volume']]

    def getStockInfoDetail(self, code, ktype, start, end):
        _st_info = tu.get_hist_data(code, ktype=ktype, start=start, end=end)
        return _st_info


if __name__ == '__main__':
    stockPool = StockPool()
    print(stockPool.st_list)
