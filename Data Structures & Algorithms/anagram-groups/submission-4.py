class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for ele in strs:
            count = [0] * 26
            for c in ele:
                count[ord(c)-ord('a')] += 1
            res[tuple(count)].append(ele)
        return list(res.values())
                
            

        