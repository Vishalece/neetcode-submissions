class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        l=[]
        nums.sort()
        for n in nums :
            if n not in mp:
                mp[n] = 1
            else :
                mp[n]+=1
        # m = dict(sorted(mp.items(),key=lambda x: x[1],reverse = True))
        # for i in m:
        #     l.append(i)
        #     if(k == len(l)) :
        #         return l
        l = sorted(mp,key = mp.get,reverse = True)[:k]
        return l
            
            
        
        

            

        
        