from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        t = defaultdict(list)

        for ch in strs:
            sorted_s = tuple(sorted(ch))
            if sorted_s in t:
                t[sorted_s].append(ch)
            else:
                t[sorted_s] = [ch]

        return t.values()