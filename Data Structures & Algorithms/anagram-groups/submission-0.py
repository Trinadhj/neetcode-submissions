class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        anagram_sublist = defaultdict(list)

        for word in strs:
            anagram = ''.join(sorted(word))
            anagram_sublist[anagram].append(word)

        return [v for k,v in anagram_sublist.items()]