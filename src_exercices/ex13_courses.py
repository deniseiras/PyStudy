from collections import defaultdict
class Solution:

    WHITE = 1
    GRAY = 2
    BLACK = 3

    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """

        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)

        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)

        topological_sorted_order = []
        is_possible = True

        # By default all vertces are WHITE
        color = {k: Solution.WHITE for k in range(numCourses)}
        def dfs(node):
            nonlocal is_possible

            # Don't recurse further if we found a cycle already
            if not is_possible:
                return

            # Start the recursion
            color[node] = Solution.GRAY

            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == Solution.WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == Solution.GRAY:
                         # An edge to a GRAY vertex represents a cycle
                        is_possible = False

            # Recursion ends. We mark it as black
            color[node] = Solution.BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == Solution.WHITE:
                dfs(vertex)

        return topological_sorted_order[::-1] if is_possible else []




#from typing import List


# class Solution:
#
#     def add_dependencies(self, visited_in_depth_search, return_list, dic, each_course, pre_requisites):
#         for dep in pre_requisites:
#             dependent = dep[0]
#             dependency = dep[1]
#             if each_course == dependency:
#                 if not each_course in dic.keys():
#                     dic[each_course] = []
#                 elif dependent in visited_in_depth_search and dependent in dic[each_course]:
#                     return True, [], dic
#                 visited_in_depth_search.append(dependent)
#                 dic[each_course].append(dependent)
#                 check_cycle, return_list, dic = self.add_dependencies(visited_in_depth_search, return_list, dic, dependent, pre_requisites)
#                 if check_cycle:
#                     return True, [], dic
#         if each_course not in return_list:
#             return_list.append(each_course)
#         return False, return_list, dic
#
#     def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#
#         courses = range(numCourses)
#         dic = {}
#         return_list = []
#
#         for curr in courses:
#             visited_in_depth_search = []
#             check_cycle, return_list, dic = self.add_dependencies(visited_in_depth_search, return_list, dic, curr, prerequisites)
#             if check_cycle:
#                 return []
#         return_list.reverse()
#
#         return return_list
