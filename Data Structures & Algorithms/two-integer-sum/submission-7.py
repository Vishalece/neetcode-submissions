class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # l = 0
        # r = len(nums)-1
        # sum =0
        # while (l < r):
        #     sum = nums[l]+nums[r]
        #     if(sum == target):
        #         return [l,r]
        #     if( sum < target):
        #         l+=1
        #     else:
        #         r-=1
        # return []

        mp = {}

        for i, num in enumerate(nums):

            comp = target - num

            if comp in mp:
                return [mp[comp],i]

            mp[num] = i

        return []
        