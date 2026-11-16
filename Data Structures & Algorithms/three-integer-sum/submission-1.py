class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        l = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                    continue
            t = -(nums[i])
            s = i+1
            e = len(nums)-1
            while(e >s):
                sum = nums[e]+nums[s]
                if( sum == t):
                    l.append([nums[i], nums[s], nums[e]])
                    e = e-1
                    s=s+1
                    while s<e and nums[s] == nums[s-1]:
                        s =s +1
                    while s<e and nums[e] == nums[e+1]:
                        e = e-1
                elif(sum > t):
                    e = e -1
                elif(sum < t):
                    s = s+1
        return l


        