import unittest
from PyStudy.src_exercices.ex14_redundant_connections import Solution

class Test(unittest.TestCase):
    # def test_bin_find_min_array(self):
    #     self.fail()

    # def test_bin_find_min_array_not_empty(self):
    #     self.fail()

    def test_happy_day(self):
        edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        real = [1,4]
        self.solution_test(edges, real)

    def test_happy_day_2(self):
        edges = [[1,2],[1,3],[2,3]]
        real = [2,3]
        self.solution_test(edges, real)

    def test_branch_appended_v1(self):
        edges = [[1,2],[2,3],[3,4],[4,5],[3,5],[1,6]]
        real = [3,5]
        self.solution_test(edges, real)

    def test_branch_appended_v2(self):
        edges = [[1,2],[2,3],[3,4],[3,5],[4,5],[1,6]]
        real = [4,5]
        self.solution_test(edges, real)

    def test_cycle_branch_on_root_with_2_childs_of_branch_and_2_childs_of_root(self):
        edges = [[1,3],[3,4],[1,5],[3,5],[2,3]]
        real = [3,5]
        self.solution_test(edges, real)

    def test_cycle_branch_on_root_with_1_childs_of_branch_and_3_childs_of_root(self):
        edges = [[1,4],[3,4],[1,3],[1,2],[4,5]]
        real = [1,3]
        self.solution_test(edges, real)

    def test_cycle_with4_branch_on_root(self):
        #    3 - 5
        #   /    |
        #  4 --- 2 - 1
        edges = [[3,4],[1,2],[2,4],[3,5],[2,5]]
        real = [2,5]
        self.solution_test(edges, real)

    def solution_test(self, edges, real_removed_edge):
        solution = Solution()
        calc = solution.findRedundantConnection(edges)
        self.assertEqual(real_removed_edge, calc)


if __name__ == '__main__':
    unittest.main()
