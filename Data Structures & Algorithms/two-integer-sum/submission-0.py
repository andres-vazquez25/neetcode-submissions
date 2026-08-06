class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        outputs={}
        
        for index, value in enumerate(nums):
            complement=target-value
            if complement in outputs:
                return [outputs[complement] , index]
                
            else:
                outputs[value]=index
        