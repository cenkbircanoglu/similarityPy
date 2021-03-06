from unittest import TestCase

from similarityPy.algorithms.find_nearest import FindNearest
from similarityPy.measure.string_data.damerau_levenshtein_distance import DamerauLevenshteinDistance
from tests import test_logger


__author__ = 'cenk'


class FindNearestTest(TestCase):
    def setUp(self):
        pass

    def test_damerau_levenshtein_distance(self):
        test_logger.debug("FindNearestTest - test_damerau_levenshtein_distance Starts")

        points = ["abcdef", "abcef", "abcde"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcdef", nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXdef", nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "123456"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXef", nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "123456 "
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals("abcXdef", nearest)

        test_logger.debug("FindNearestTest - test_damerau_levenshtein_distance Ends")

    def test_damerau_levenshtein_distance_multiple(self):
        test_logger.debug("FindNearestTest - test_damerau_levenshtein_distance_multiple Starts")

        points = ["abcdef", "abcef", "abcde"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcdef', 'abcef'], nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "abcdefg"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXdef', 'abcXdef'], nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "123456"
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXef', 'abcXef'], nearest)

        points = ["abcXdef", "abcXef", "abcXde"]
        point = "123456 "
        find_nearest = FindNearest(points, point, DamerauLevenshteinDistance, k=2)
        find_nearest.process()
        nearest = find_nearest.get_result()
        self.assertEquals(['abcXdef', 'abcXdef'], nearest)

        test_logger.debug("FindNearestTest - test_damerau_levenshtein_distance_multiple Ends")