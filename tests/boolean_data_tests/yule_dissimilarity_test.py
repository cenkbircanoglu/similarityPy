# coding=utf-8
from unittest import TestCase

from apps.distances.boolean_data.yule_dissimilarity import YuleDissimilarity

from tests import test_logger


__author__ = 'cenk'


class YuleDissimilarityTest(TestCase):
    def test_algorithm(self):
        test_logger.debug("YuleDissimilarityTest - test_algorithm Starts")
        data = [[1, 0, 1, 1, 0], [1, 1, 0, 1, 1]]
        dice_dissimilarity = YuleDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(2.0, result)

        data = [[True, False, True], [True, True, False]]
        dice_dissimilarity = YuleDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(2, result)

        data = [[0, 0, 0, 0], [0, 0, 0, 0]]
        dice_dissimilarity = YuleDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(0.0, result)

        data = [[0, 1, 0, 1], [1, 0, 1, 0]]
        dice_dissimilarity = YuleDissimilarity(data)
        dice_dissimilarity.process()
        result = dice_dissimilarity.get_result()
        self.assertEquals(2.0, result)

        data = [[3], [4, 5, 6]]
        dice_dissimilarity = YuleDissimilarity(data)
        with self.assertRaises(ArithmeticError) as context:
            dice_dissimilarity.process()
        self.assertEqual('You cant calculate Yule dissimilarity of array has different sizes.',
                         context.exception.message)
        test_logger.debug("YuleDissimilarityTest - test_algorithm Ends")
