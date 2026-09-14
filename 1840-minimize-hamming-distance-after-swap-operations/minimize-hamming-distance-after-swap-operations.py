class Solution:
    def minimumHammingDistance(self, source, target, allowedSwaps):
        n = len(source)

        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(a, b):
            rootA = find(a)
            rootB = find(b)

            if rootA != rootB:
                parent[rootB] = rootA

        # Connect all indices that can be swapped
        for a, b in allowedSwaps:
            union(a, b)

        # Count source values in each connected group
        groups = {}

        for i in range(n):
            root = find(i)

            if root not in groups:
                groups[root] = {}

            value = source[i]
            groups[root][value] = groups[root].get(value, 0) + 1

        # Calculate minimum Hamming distance
        answer = 0

        for i in range(n):
            root = find(i)
            value = target[i]

            if groups[root].get(value, 0) > 0:
                groups[root][value] -= 1
            else:
                answer += 1

        return answer