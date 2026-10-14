class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_subset = defaultdict(list)

        for word in strs:
            anagram = ''.join(sorted(word))
            anagram_subset[anagram].append(word)

        return [v for k,v in anagram_subset.items()]