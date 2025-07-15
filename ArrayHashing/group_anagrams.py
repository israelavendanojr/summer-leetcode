class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            key = tuple(count)
            hash[key].append(s)
        
        return list(hash.values())
        
        
# REDO : 7/15/2025
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First Attempt : 15:02 -> DNF
        # Second Attempt : 

        hash = defaultdict(list)

        # Every word
        for s in strs:
            count = [0] * 26

            # Creating count every for that word, go through every char
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            # array and hash are immutable, cant be hashed, convert to tuple before adding to hash
            key = tuple(count)
            hash[key].append(s)

        res = []
        for val in hash.values():
            res.append(val)

        return res

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Time 4:34
        map = defaultdict(list)

        for s in strs:
            count = [0] * 26
            for c in s:
                index = ord(c) - ord('a')
                count[index] += 1

            key = tuple(count)
            map[key].append(s)

        return list(map.values())
