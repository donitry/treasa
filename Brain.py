#!/usr/bin/env python
# encoding: utf-8

import tushare as tu, numpy as np, pandas as pd, random

class StockPool:
    def __init__(self):
        self.st_list = tu.get_sz50s()

    def choiceOneStock(self):
        _st = random.choice(self.st_list['code'].tolist())
        return _st


if __name__ == '__main__':
    _cst = StockPool()
    print(_cst.choiceOneStock())

