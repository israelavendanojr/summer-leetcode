class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Time 04:16
        max_len = 0
        counter = {}

        l = 0
        for r in range(len(s)):
            counter[s[r]] = 1 + counter.get(s[r], 0)

            # window_len - most_freq_char > k
            while ((r-l+1) - max(counter.values())) > k:
                counter[s[l]] = counter.get(s[l], 0) - 1
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len