class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        final_list = []
        strs_passed = set()
        for index1, ele in enumerate(strs):
            if ele in strs_passed:
                continue
            new_list = []
            new_list.append(ele)
            strs_passed.add(ele)
            for index2 in range(index1+1,len(strs)):
                next_ele = strs[index2]
                if sorted(ele)==sorted(next_ele):
                    new_list.append(next_ele)
                    strs_passed.add(next_ele)
            final_list.append(new_list)


        return final_list