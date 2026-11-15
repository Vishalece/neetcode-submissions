class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num = set(nums)
        max_len = 0
        for i in num :              
            if (i-1) not in num:
                l = 1
                start = i
                while((start+1) in num):
                    l = l +1
                    start = start + 1
                max_len = max(max_len,l)
        return max_len

        # nums = sorted(list(set(nums)))  
        # l=[]
        # mp = {}
        # # l.append(nums[0])
        # if(len(nums) < 2):
        #     return len(nums)
        # for i in range(1,len(nums)):
        #     if((nums[i]-1) == nums[i-1]) :
        #         if(len(l) == 0) :
        #             l.append(nums[i-1])
        #         l.append(nums[i])
        # for i in range(1,len(nums)) :
        #     if(nums[i-1] == (nums[i] - 1)) :
        #         if(len(l) == 0) :
        #             l.append(nums[i-1])
        #             # l.append(nums[i])
        #             mp[count] = l
        #         else :
        #             mp[count].append(nums[i-1])
        #     else :
        #         mp[count] = []
        #         l = [] 
        # if ( ((nums[len(nums) - 1]) - 1 ) == ((nums[len(nums)-2]))) :
        #     mp[count].append(nums[len(nums) - 1])
        
        # return(len(mp[count]))
                
        