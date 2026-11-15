class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # res = defaultdict(list)
        # for s in strs :
        #     count = [0]*26
        #     for c in s :
        #         count[ord(c)-ord("a")] += 1
        #     res[tuple(count)].append(s)
        
        # return list(res.values())
        mp = {}
        for s in strs:
            str = "".join(sorted(s))
            if str in mp :
                mp[str].append(s)
            else:
                mp[str] = [s]
        return list(mp.values())

            



        
        



        