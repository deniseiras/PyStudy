from collections import defaultdict
from typing import List


class Solution:

    class Graph:
        WHITE = 1
        GRAY = 2

        def __init__(self, edges):
            self.edges = defaultdict(list)
            self.color = {}
            self.path_to_cycle = []
            for edge in edges:
                self.edges[edge[0]].append(edge[1])
                self.edges[edge[1]].append(edge[0])
                self.color[edge[0]] = self.WHITE
                self.color[edge[1]] = self.WHITE

        def dep_search(self, vert, cycle_found):

            if cycle_found:
                return cycle_found
            else:
                if self.color[vert] == self.WHITE:
                    self.color[vert] = self.GRAY
                    self.path_to_cycle.append(vert)

                    if len(self.path_to_cycle) > 2:
                        intersect = [each for each in self.edges[vert] if each in self.path_to_cycle[:-2]]
                        if len(intersect) == 1:
                            self.path_to_cycle.append(intersect[0])
                            return True

                    for c_vert in self.edges[vert]:
                        cycle_found = self.dep_search(c_vert, cycle_found)
                        if cycle_found:
                            return cycle_found
                    self.path_to_cycle.pop()

        def get_cycle_edges(self):
            root_vert = 1

            if self.dep_search(root_vert, False):
                cycle_edges_rev = []
                cycle_vert = self.path_to_cycle.pop()
                vert_ant = self.path_to_cycle.pop()
                cycle_edges_rev.append([min(cycle_vert, vert_ant), max(cycle_vert, vert_ant)])
                for vert in reversed(self.path_to_cycle):
                    cycle_edges_rev.append([min(vert, vert_ant), max(vert_ant, vert)])
                    if vert == cycle_vert:
                        break
                    vert_ant = vert
            # else is already a tree - never
            else:
                raise Exception('Must allways find a cycle graph!')

            return cycle_edges_rev

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # 1. create graph with edges
        graph = self.Graph(edges)

        # 2. depth search to find a cycle and store the edges of the cycle
        cycle_rev = graph.get_cycle_edges()

        # 3. Look for the last edge of the cycle contained in the graph edges
        for edge in reversed(edges):
            for edge_cycle in cycle_rev:
                if edge_cycle == edge:
                    return edge
        raise Exception('No edges found')

