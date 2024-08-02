import sys
import inspect
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        solution = []
        length = len(nums)

        def dfs(index, subset):
            print("index = ", index, "------------------------------------------")
            i = sys._getframe(0).f_locals['index']
            print("i = ", i, "------------------------------------------")
            print("get_frames = ", sys._getframe(0), "------------------------------------------")
            print("current_frames = ", sys._current_frames(), "------------------------------------------")

            if index == length:
                solution.append(subset.copy())
                return

            dfs(index + 1, subset.copy())
            subset.append(nums[index])
            dfs(index + 1, subset.copy())

        dfs(0, [])
        return solution