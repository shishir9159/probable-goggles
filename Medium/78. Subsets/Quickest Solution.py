class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        solution = []
        length = len(nums)

        def dfs(index, permutation):
            if index == length:
                solution.append(permutation.copy())
                return
        
            permutation.append(nums[index])
            dfs(index + 1, permutation)
            permutation.pop()
            dfs(index + 1, permutation)
        
        dfs(0, [])
        return solution