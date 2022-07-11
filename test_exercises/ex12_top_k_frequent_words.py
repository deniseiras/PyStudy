import unittest
from PyStudy.src_exercices.ex12_top_k_frequent_words import Solution


class Test(unittest.TestCase):
    # def test_bin_find_min_array(self):
    #     self.fail()

    # def test_bin_find_min_array_not_empty(self):
    #     self.fail()

    def test_happy_day(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 4
        real = ["the","is","sunny","day"]
        self.solution_test(words, k, real)

    def test_k1(self):
        words = ["the"]
        k = 1
        real = ["the"]
        self.solution_test(words, k, real)

    def test_k_exceeds(self):
        words = ["the"]
        k = 10
        real = ["the"]
        self.solution_test(words, k, real)

    def test_k0(self):
        words = ["the","day","is","sunny","the","the","the","sunny","is","is"]
        k = 0
        real = []
        self.solution_test(words, k, real)

    def test_same_k_alpha_order(self):
        words = ["the", "day", "is", "sunny", "and", "nice", "the", "day"]
        k = 6
        real = ["day", "the", "and", "is", "nice", "sunny"]
        self.solution_test(words, k, real)

    def test_same_k_alpha_order_k2(self):
        words = ["i", "love", "leetcode", "i", "love", "coding"]
        k = 2
        real = ["i","love"]
        self.solution_test(words, k, real)


    def solution_test(self, words, k, real):
        solution = Solution()
        calc = solution.topKFrequent(words, k)
        self.assertEqual(real, calc)


if __name__ == '__main__':
    unittest.main()
