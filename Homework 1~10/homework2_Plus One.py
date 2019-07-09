
class Solution:
    def plusOne(self, digits):
        a=""
        for i in digits:
            a+=str(i)
        a = int(a) + 1
        b = []
        for i in str(a):
            b.append(int(i))
        digits = b
        return digits