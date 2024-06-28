speed comparisons between [nums[:]] and [nums.copy()]

explain why this doesn't work:
```
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
           
            permutations = self.permute(nums[1:])

            for permutation in permutations:
                permutation.append(nums[0])
            result.extend(permutations)

        return result
```