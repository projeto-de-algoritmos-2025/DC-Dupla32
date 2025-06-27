MOD = 10**9 + 7

class Solution(object):
    def maximumSumSubsequence(self, nums, queries):
        n = len(nums)
        seg = [[0] * 4 for _ in range(4 * n)]

        def push_up(ind):
            l = 2 * ind + 1
            r = 2 * ind + 2

            seg[ind][0] = max(
                seg[l][0] + seg[r][0],
                seg[l][1] + seg[r][0],
                seg[l][0] + seg[r][2]
            )
            seg[ind][1] = max(
                seg[l][0] + seg[r][1],
                seg[l][1] + seg[r][1],
                seg[l][0] + seg[r][3]
            )
            seg[ind][2] = max(
                seg[l][2] + seg[r][0],
                seg[l][3] + seg[r][0],
                seg[l][2] + seg[r][2]
            )
            seg[ind][3] = max(
                seg[l][2] + seg[r][1],
                seg[l][3] + seg[r][1],
                seg[l][2] + seg[r][3]
            )

        def build(ind, low, high):
            if low == high:
                seg[ind][0] = 0
                seg[ind][1] = float('-inf')
                seg[ind][2] = float('-inf')
                seg[ind][3] = max(0, nums[low])  
                return
            mid = (low + high) // 2
            build(2 * ind + 1, low, mid)
            build(2 * ind + 2, mid + 1, high)
            push_up(ind)

        def update(ind, low, high, k, val_update):
            if low > k or high < k:
                return
            if low == high:
                seg[ind][0] = 0
                seg[ind][1] = float('-inf')
                seg[ind][2] = float('-inf')
                seg[ind][3] = max(0, val_update)
                return
            mid = (low + high) // 2
            update(2 * ind + 1, low, mid, k, val_update)
            update(2 * ind + 2, mid + 1, high, k, val_update)
            push_up(ind)

        build(0, 0, n - 1)

        result = 0
        for k, val in queries:
            update(0, 0, n - 1, k, val)
            result = (result + max(seg[0])) % MOD

        return result
