class Solution:
    def distance(self, nums):
        positions = {}

        for i, num in enumerate(nums):
            if num not in positions:
                positions[num] = []
            positions[num].append(i)

        answer = [0] * len(nums)

        for indices in positions.values():
            total = sum(indices)
            count = len(indices)
            left_sum = 0

            for k, index in enumerate(indices):
                right_sum = total - left_sum - index

                left_count = k
                right_count = count - k - 1

                answer[index] = (
                    index * left_count - left_sum
                    + right_sum - index * right_count
                )

                left_sum += index

        return answer