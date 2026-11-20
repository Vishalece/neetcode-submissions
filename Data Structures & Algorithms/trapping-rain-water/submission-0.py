class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        max_left = 0
        max_right = 0
        result = 0
        while(r>l):
            if(height[l] < height[r]):
                max_left = max(max_left,height[l])
                val = max_left - height[l]
                result = result + val
                l = l+1
            else :
                max_right = max(max_right,height[r])
                val = max_right - height[r]
                result = result + val
                r = r- 1
        return result




        