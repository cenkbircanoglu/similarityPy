# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import math

from similarityPy.algorithms.variance import Variance


class StandartDeviation:
    def __init__(self):
        self._data = []

    def calculate(self, data, is_tuple=False, index=None):
        if is_tuple:
            self._data = sorted([float(obj[index]) for obj in data])
        else:
            self._data = sorted(data)

        return self.__algorithm()

    def __algorithm(self):
        variance = Variance()
        return round(math.pow(variance.calculate(self._data), 0.5), 4)