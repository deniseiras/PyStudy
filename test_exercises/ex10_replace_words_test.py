import unittest
from PyStudy.src_exercices.ex10_replace_words import Solution


class TestReplaceWord(unittest.TestCase):
    # def test_bin_find_min_array(self):
    #     self.fail()

    # def test_bin_find_min_array_not_empty(self):
    #     self.fail()

    def test_happy_day(self):
        dictionary = ["cat", "bat", "rat"]
        sentence = "the cattle was rattled by the battery"
        real_str = "the cat was rat by the bat"
        self.replace_word_testing(dictionary, real_str, sentence)

    def test_unique_words(self):
        dictionary = ['a', 'b', 'c']
        sentence = 'aadsfasf absbs bbab cadsfafs'
        real_str = 'a a b c'
        self.replace_word_testing(dictionary, real_str, sentence)

    def test_root_in_another_root(self):
        dictionary = ['c', 'bat', 'rat', 'cat']
        sentence = 'the cattle was rattled by the battery'
        real_str = 'the c was rat by the bat'
        self.replace_word_testing(dictionary, real_str, sentence)

    def test_leet_code_fail(self):
        dictionary = ["a", "aa", "aaa", "aaaa"]
        sentence = 'baba a aa a aaaa aaa aaa aaa aaaaaa bbb ababa'
        real_str = 'baba a a a a a a a a bbb a'
        self.replace_word_testing(dictionary, real_str, sentence)

    def replace_word_testing(self, dictionary, real_str, sentence):
        solution = Solution()
        calc_str = solution.replaceWords(dictionary, sentence)
        self.assertEqual(real_str, calc_str)


if __name__ == '__main__':
    unittest.main()
