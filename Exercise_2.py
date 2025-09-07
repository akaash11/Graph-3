# S30 Problem #194 find celebrity 
#LeetCode #277 https://leetcode.com/problems/find-the-celebrity/description/

# Author : Akaash Trivedi
# Did this code successfully run on Leetcode :  Yes #
# Any problem you faced while coding this : No

# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

# topological sort 
# indegrees array: (a,b) a knows b
# increase the indegree of person b and degreees indegree of person a
# Person whos indegree is n-1, meaning that everyone knows that person => celebrity
# TC: O(n^2)
# SC: O(n)
class Solution:
    def findCelebrity(self, n: int) -> int:
        indegree = [0] * n

        for i in range(n):
            for j in range(n):
                if i == j: continue
                if knows(i, j):
                    # increase the j's indegree and decrease i's
                    indegree[j] += 1
                    indegree[i] -= 1

        # anyone has indegree n-1, means everyone knows that person 
        for i in range(n):
            if indegree[i] == n - 1:
                return i

        return -1


# linear 3n solution
# Assume one of them is a celeb, and update the celeb when they knows someone
# after 1st pass, we found some celeb: check if everyone knows celeb; celeb knows no one
# return the celeb, if not return -1
# TC: O(n)
# SC: O(1)

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0  # assume starting with 0 is celebrity
        for i in range(1, n):
            if knows(celeb, i):
                # celebrity cant know anyone, move the celebrity to i
                celeb = i

        # celeberity should not know anyone and everyone should know celeb
        for i in range(n):
            if i == celeb:continue
            if not knows(i, celeb) or knows(celeb, i):
                return -1

        return celeb


# linear 3n solution - little faster
# Assume one of them is a celeb, and update the celeb when they knows someone
# after 1st pass, we found some celeb: check if everyone knows celeb; celeb knows no one
# return the celeb, if not return -1
# TC: O(n)
# SC: O(1)

class Solution:
    def findCelebrity(self, n: int) -> int:
        celeb = 0  # assume starting with 0 is celebrity
        for i in range(1, n):
            if knows(celeb, i):
                # celebrity cant know anyone, move the celebrity to i
                celeb = i

        # celeberity should not know anyone and everyone should know celeb
        for i in range(n):
            if i == celeb:continue
            if not knows(i, celeb):
                return -1
            if i < celeb and knows(celeb, i):
                return -1
        return celeb
