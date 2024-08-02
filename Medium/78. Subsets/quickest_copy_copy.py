import inspect
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        solution = []
        length = len(nums)

        def dfs(index, subset):
            if index == length:
                solution.append(subset.copy())
                # print(index, " = ", inspect.currentframe())
                return

            dfs(index + 1, subset.copy())
            subset.append(nums[index])
            dfs(index + 1, subset.copy())

        return solution