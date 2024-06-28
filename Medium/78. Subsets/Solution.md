why it doesn't work?
```
dfs(index + 1, permutation)
permutation.append(nums[index])
dfs(index + 1, permutation)
```

check if this is faster:
```
permutation = []
def dfs(index, permutation):
    if index == length:
    solution.append(permutation.copy())
```
