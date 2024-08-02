why it doesn't work?
```
dfs(index + 1, permutation)
permutation.append(nums[index])
dfs(index + 1, permutation)
```

check if this is faster:k
```
permutation = []
def dfs(index, permutation):
    if index == length:
    solution.append(permutation.copy())
```

Performance testing:
```
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        solution = []
        length = len(nums)

        def dfs(current_state, index):
            if (length == index):
                solution.append(current_state.copy())
                return

            dfs(current_state.copy(), index + 1)
            current_state.append(nums[index])
            dfs(current_state.copy(), index + 1)

        dfs([], 0)
        return solution
```

https://www.youtube.com/watch?v=riO8Rgunc0o
https://www.youtube.com/watch?v=IxQHWt0GpsU
https://www.youtube.com/watch?v=bsyjSW46TDg
https://www.youtube.com/watch?v=xLc5xPYGGnQ
https://www.youtube.com/watch?v=QxaOlmv79ls
https://www.youtube.com/watch?v=0Om2gYU6clE
https://www.youtube.com/watch?v=3GNnVSTtl-o&list=PLFE1rxhwe5KYpTdwrE9M8ogWaSohSUpsW
Decorators

https://medium.com/@ewho.ruth2014/mastering-python-decorators-a-comprehensive-guide-for-enhancing-code-modularity-and-818ae455260d
https://devmessias.github.io/post/python_decorator_that_exposes_locals/
https://www.freecodecamp.org/news/the-python-decorator-handbook/
https://medium.com/@genexu/extracting-the-wrapped-function-from-a-decorator-on-python-call-stack-2ee2e48cdd8e
https://www.youtube.com/watch?v=-TdrFjDJn5E
https://medium.com/@morevinyl/cool-python-execute-code-on-variable-change-simple-observer-cafb88d2ec3
https://dev.to/askyt/python-callback-when-variable-changes-5bii
https://stackoverflow.com/questions/51885246/callback-on-variable-change-in-python
https://github.com/sparshg/animations?tab=readme-ov-file
