class Solution(object):
    def createSortedArray(self, instructions):
        """
        :type instructions: List[int]
        :rtype: int
        """
        MOD = 10 ** 9 + 7
        
        class FenwickTree:
            def __init__(self, size):
                self.tree = [0] * (size + 2)
                self.size = size + 2

            def update(self, i, delta):
                while i < self.size:
                    self.tree[i] += delta
                    i += i & -i

            def query(self, i):
                res = 0
                while i > 0:
                    res += self.tree[i]
                    i -= i & -i
                return res

        max_val = max(instructions)
        BIT = FenwickTree(max_val)
        cost = 0

        for i, num in enumerate(instructions):
            less = BIT.query(num - 1)
            greater = i - BIT.query(num)
            cost += min(less, greater)
            cost %= MOD
            BIT.update(num, 1)

        return cost
