
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True        
        num = 1        
        while 1:
            num=num*2
            if n == num:
                return True
            elif num > n:
                return False