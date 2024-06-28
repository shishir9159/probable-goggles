why the code doesn't run if I change the order of backtracking from:

```
current_combination.append(candidates[index])
dfs(index, current_combination, summation + candidates[index])
current_combination.pop()
dfs(index + 1, current_combination, summation)
```
to
```
dfs(index + 1, current_combination, summation)
current_combination.append(candidates[index])
dfs(index, current_combination, summation + candidates[index])
```
