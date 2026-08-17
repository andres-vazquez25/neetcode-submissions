class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_without_duplicates=[]

        for i in nums:
            if i in nums_without_duplicates:
                return True
            else:
                nums_without_duplicates.append(i)
        return False