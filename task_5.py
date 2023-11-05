def task_5(stamp, target):
    def can_stamp(start):
        stamped = False
        for i in range(len(stamp)):
            if target[start + i] == '?':
                continue
            if target[start + i] != stamp[i]:
                return False
            stamped = True
        if stamped:
            for i in range(len(stamp)):
                target[start + i] = '?'
            return True
        return False

    n, m = len(target), len(stamp)
    ans = []
    target = list(target)
    done = 0

    for _ in range(10 * n):
        stamped = False
        for i in range(n - m + 1):
            if target[i] == '?':
                continue
            if can_stamp(i):
                ans.append(i)
                done += 1
                stamped = True
                if done == n:
                    return ans[::-1]
        if not stamped:
            return []

    return []


stamp = "abc"
target = "ababc"
result = task_5(stamp, target)
print(result) 
