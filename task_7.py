def task_7(nums, k):
    n = len(nums)
    dp = [0] * n
    result = nums[0]

    for i in range(n):
        max_sum = 0
        for j in range(1, k + 1):
            if i - j >= 0:
                max_sum = max(max_sum, dp[i - j])
        dp[i] = max(max_sum, 0) + nums[i]
        result = max(result, dp[i])

    return result


nums1 = [10, 2, -10, 5, 20]
k1 = 2
print(task_7(nums1, k1)) 

nums2 = [-1, -2, -3]
k2 = 1
print(task_7(nums2, k2)) 

nums3 = [10, -2, -10, -5, 20]
k3 = 2
print(task_7(nums3, k3))  
