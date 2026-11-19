class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        vis = 0
        while(l<r):
            w = (r-l)
            v= min(heights[l],heights[r])
            p = w*v
            vis = max(vis,p)
            if(heights[l] < heights[r]):
                l = l + 1
            else:
                r =r - 1
        return vis
        