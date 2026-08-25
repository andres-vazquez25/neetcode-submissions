class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            num = 0
            for digit in str(n):
                num += int(digit)**2
            if num in seen:
                return False
            seen.add(num)
            n = num

        return True