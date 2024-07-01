from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        solution = []
        length = len(nums)

        def dfs(index, subset):
            if index == length:
                solution.append(subset.copy())
                return
            
            subset.append(nums[index])
            dfs(index + 1, subset)
            subset.pop()
            dfs(index + 1, subset)

        dfs(0, [])
        return solution