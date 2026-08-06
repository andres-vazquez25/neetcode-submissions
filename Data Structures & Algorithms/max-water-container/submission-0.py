class Solution:
    def maxArea(self, heights: List[int]) -> int:
    
        left=0
        right=len(heights)-1
        max_water=0
        
        while left<right:
            min_area=min(heights[left], heights[right])
            water=min_area*(right-left)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
            max_water=max(water,max_water)
        return max_water
        