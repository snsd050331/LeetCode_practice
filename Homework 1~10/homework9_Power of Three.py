
class Solution:
    def isPowerOfThree(self, n):
        if n == 1:
            return True        
        num = 1        
        while 1:
            num=num*3
            if n == num:
                return True
            elif num > n:
                return False