class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        solution = []
        length = len(candidates)

        def dfs(index, current_combination, summation):

            if target == summation:
                solution.append(current_combination.copy())
                return

            if index == length or summation > target:
                return

            current_combination.append(candidates[index])
            dfs(index, current_combination, summation + candidates[index])
            current_combination.pop()
            dfs(index + 1, current_combination, summation)

        dfs(0, [], 0)

        return solution