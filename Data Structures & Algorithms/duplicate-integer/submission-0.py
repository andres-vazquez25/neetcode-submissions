class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        list_of_nums={}

        for number in nums:
            if number in list_of_nums:
                return True
            else:
                list_of_nums[number]=1
        return False
                