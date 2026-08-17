class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_without_duplicates=set()

        for i in nums:
            if i not in nums_without_duplicates:
                nums_without_duplicates.add(i)
            else:
                return True
        return False