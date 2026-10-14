class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict

        freq_dict = defaultdict(int)
        max_substring = 0
        i = 0
        for j in range(len(s)):
            while freq_dict[s[j]] > 0:
                freq_dict[s[i]] -= 1
                i += 1
            freq_dict[s[j]] += 1
            print(j,i)
            max_substring = max(max_substring, j-i+1)
        return max_substring