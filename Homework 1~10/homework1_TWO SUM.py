
class Solution:
    def twoSum(self, nums, target):
        dic=dict()
        for index, value in enumerate(nums):
            sub = target - value
            if sub in dic:
                return [dic[sub], index]
            else:
                dic[value] = index
if __name__ == '__main__':
    nums=[2, 7, 11, 15]
    print(type(nums))
    target = 9
    result = Solution().twoSum(nums, target)
    print(result)