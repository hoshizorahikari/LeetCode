"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]

数组，哈希表
"""


class Solution:
    def twoSum_2(self, nums, target):
        # O(n^2),超时
        n = len(nums)
        for i in range(n - 1):
            for j in range(1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target):
        d = {}  # 数字为key, 下标为value
        for i in range(len(nums)):
            if not nums[i] in d:
                d[nums[i]] = i
            if target - nums[i] in d:
                # 可能出现nums[i]*2=target的情况,此时j=i,不符合;所以另一个下标j要在i之前
                j = d[target - nums[i]]
                if j < i:
                    return [j, i]


if __name__ == '__main__':
    nums = [3, 2, 4, 2]
    print(Solution().twoSum(nums, 4))  # [1, 3]
