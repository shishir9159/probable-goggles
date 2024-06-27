class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        length = len(nums)
        solution = []

        def dfs(index, current, summation):
            if target == summation:
                solution.append(current.copy())
                return
            elif index == length or summation > target:
                return

            current.append(nums[index])
            dfs(index, current, summation + nums[index])
            current.pop()
            dfs(index + 1, current, summation)

        dfs(0, [], 0)

        return solution