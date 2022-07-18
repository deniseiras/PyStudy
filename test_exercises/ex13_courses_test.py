import unittest
from PyStudy.src_exercices.ex13_courses import Solution

class Test(unittest.TestCase):
    # def test_bin_find_min_array(self):
    #     self.fail()

    # def test_bin_find_min_array_not_empty(self):
    #     self.fail()

    def test_happy_day(self):
        numCourses = 4
        prerequisites = [[1,0],[2,0],[3,1],[3,2]]
        real = [0,2,1,3]
        self.solution_test(numCourses, prerequisites, real)

    def test_no_prereq(self):
        numCourses = 1
        prerequisites = []
        real = [0]
        self.solution_test(numCourses, prerequisites, real)

    def test_one_req_four_courses(self):
        numCourses = 4
        prerequisites = [[1, 0]]
        real = [3,2,0,1]
        self.solution_test(numCourses, prerequisites, real)

    def test_chain(self):
        numCourses = 4
        prerequisites = [[3, 2], [2, 1], [1, 0]]
        real = [0,1,2,3]
        self.solution_test(numCourses, prerequisites, real)

    def test_chain_rev(self):
        numCourses = 6
        prerequisites = [[0, 1], [1, 2], [2, 3]]
        real = [5, 4, 3, 2, 1, 0]
        self.solution_test(numCourses, prerequisites, real)

    def test_cycle(self):
        numCourses = 2
        prerequisites = [[0, 1], [1, 0]]
        real = []
        self.solution_test(numCourses, prerequisites, real)

    def test_cycle_2(self):
        numCourses = 3
        prerequisites = [[0, 1], [1, 2], [2, 0]]
        real = []
        self.solution_test(numCourses, prerequisites, real)

    def solution_test(self, numCourses, prerequisites, real):
        solution = Solution()
        calc = solution.findOrder(numCourses,prerequisites)
        self.assertEqual(real, calc)


if __name__ == '__main__':
    unittest.main()
