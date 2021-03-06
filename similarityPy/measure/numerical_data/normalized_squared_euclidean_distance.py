# coding=utf-8
"""
Created on 18 January 2014
@author: Cenk Bircanoglu
"""
import operator

from similarityPy.algorithms.mean import Mean
from similarityPy.measure.similarity_measure import SimilarityMeasure
from similarityPy.measure.similarity_measure_type import SimilarityMeasureType


class NormalizedSquaredEuclideanDistance(SimilarityMeasure):
    similarity_measure_type = SimilarityMeasureType.DISTANCE_ABBR

    def _algorithm(self):
        if len(self._data) == 2:
            point_a = self._data[0]
            point_b = self._data[1]
            if len(point_a) == len(point_b):
                mean = Mean()
                mean_b = mean.calculate(point_b)
                mean_a = mean.calculate(point_a)
                try:
                    dividend = sum(
                        ((float(c) + mean_b - mean_a )) ** 2 for c in map(operator.sub, point_a, point_b))
                    divider = 2 * (
                        sum((float(c) - mean_a ) ** 2 for c in point_a) + sum(
                            (float(c) - mean_b ) ** 2 for c in point_b))
                    self._result = (dividend / divider)
                except ArithmeticError:
                    raise ArithmeticError("float division by zero")
            else:
                raise ArithmeticError(
                    "You cant calculate Normalized Squared Euclidean distance of array has different sizes.")
        else:
            raise ArithmeticError("You must enter two array to find Normalized Squared Euclidean distance.")