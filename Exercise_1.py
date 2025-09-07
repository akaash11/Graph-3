# S30 Problem #216 Optimize Water Distribution in a Village
#LeetCode #1168 https://leetcode.com/problems/optimize-water-distribution-in-a-village/

# Author : Akaash Trivedi
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# union find technique
# connect the village node to a dummy node 0 with cost of wells as edge
# add pipe to edges and sort them according to cost
# use union find to connect each nodes until all nodes are connected and return result
# TC: O(E log E) Here E = edges
# SC: O(E + V)
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:
        edges = []
        uf = []  # union find
        for i in range(n+1):
            uf.append(i)
        # make a dummy node 0 and draw edges from it to each node and give well cost
        for i in range(1,n+1):
            # edge from 0 to, node, cost of well
            edges.append((0, i, wells[i-1]))
        
        # add pipes cost to edges
        edges.extend(pipes)
        edges.sort(key=lambda x:x[2])
        print(edges)
        
        res = 0
        for edge in edges:
            x, y = edge[0], edge[1]
            px = self.find(uf, x)  # parent x
            py = self.find(uf, y)  # parent y

            if px != py:
                res += edge[2]
                uf[py] = px
        
        return res
    
    # function to find ulimate parent
    def find(self, uf, x):
        # base
        if x != uf[x]:
            uf[x] = self.find(uf, uf[x])
        return uf[x]