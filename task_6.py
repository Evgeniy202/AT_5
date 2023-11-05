from collections import deque

def task_6(nums, k):
    if not nums:
        return []

    max_values = []
    window = deque()

    for i, num in enumerate(nums):
        while window and nums[window[-1]] < num:
            window.pop()
        window.append(i)

        if i - window[0] >= k:
            window.popleft()

        if i >= k - 1:
            max_values.append(nums[window[0]])

    return max_values


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
result = task_6(nums, k)
print(result)  
