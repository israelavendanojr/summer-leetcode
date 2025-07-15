class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counter = Counter(nums)

        for count in counter:
            index = counter[count]
            freq[index].append(count)

        res = []
        for i in range(len(freq) - 1, -1, -1):
            for j in freq[i]:
                res.append(j)
                if len(res) == k:
                    return res


# REDO : 7/15/2025
# First Attempt : 16:37 -> DNF

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time 6:31
        count = Counter(nums)
        freq = [[] for i in range(len(nums) + 1)] 

        # assign buckets
        for c in count:
            freq[count[c]].append(c)

        res = []
        # iterate buckets backwards
        for i in range(len(freq) - 1, 0, -1):
            # interate each bucket and stop at K elemtents
            for j in range(len(freq[i])):
                if len(res) < k:
                    res.append(freq[i][j])
                else:
                    break

        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Time : 8:02
        count = Counter(nums)
        buckets = [[] for i in range(len(nums) + 1)]

        for c in count:
            buckets[count[c]].append(c)

        res = []
        for i in range(len(buckets) - 1, 0, - 1):
            for j in range(len(buckets[i])):
                res.append(buckets[i][j])
                if len(res) == k:
                    return res
