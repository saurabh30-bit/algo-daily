def permute(nums):
    res = []
    def dfs(path, used):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i, num in enumerate(nums):
            if not used[i]:
                used[i] = True
                path.append(num)
                dfs(path, used)
                path.pop()
                used[i] = False
    dfs([], [False]*len(nums))
    return res
