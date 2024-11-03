#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Name: 
    268 contains duplicates

Version:
	0.0.1

Summary:
    My solution along with a more optimal solution to the problem from leetcode

Problem Pattern(s):
    Arrays, Bit Manipulation

Author:
    Luke Marren

License: 
    MIT

Requires:
    typing

Date Last Modified:
	November 3, 2024
"""

from typing import List


class MyFirstSolution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Return a missing value among an unsorted list with bounds 0 to n.

        Args:
            nums (List[int]): a given array of distinct ints with length .

        Returns:
            bool: True for duplicates, false for all distinct values.

        Solution Stats:
            Time spent: 6 minutes
            Runtime: 1289ms, beats 15.63%, O(n)
            Memory: 17.66MB, beats 85.67%, O(1)
        """

        # Loop through range that is upper-bound inclusive of length of nums
        for i in range(len(nums) + 1):

            # If an index is not in nums, return it
            if i not in nums:
                return i


class XorSum:
    def missingNumber(self, nums: List[int]) -> int:
        """
        Solution Stats:
            Runtime: 1ms, beats 70.55%, O(n)
            Memory: 17.51MB, beats 97.56%, O(1)
        """
        sum = 0
        n = len(nums)
        
        # If every value in the array were present, the XORs would cancel to 0
        # Even though nums is out of order, every number that exists in the array will eventually pari up and cancel out with its corresponding index
        # The only number that does not get canceled out is the missing one 

        for i in range(n):
            sum ^= i ^ nums[i]
        return sum ^ n
