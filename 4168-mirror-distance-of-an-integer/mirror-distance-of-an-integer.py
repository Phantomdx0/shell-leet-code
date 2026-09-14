class Solution:
    def mirrorDistance(self, n):
        reverse = int(str(n)[::-1])
        return abs(n - reverse)