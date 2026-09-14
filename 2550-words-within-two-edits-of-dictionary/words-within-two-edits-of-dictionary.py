class Solution:
    def twoEditWords(self, queries, dictionary):
        answer = []

        for query in queries:
            for word in dictionary:
                count = 0

                for i in range(len(query)):
                    if query[i] != word[i]:
                        count += 1

                    if count > 2:
                        break

                if count <= 2:
                    answer.append(query)
                    break

        return answer