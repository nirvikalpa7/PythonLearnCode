from typing import List

# 169. Majority Element
# https://leetcode.com/problems/majority-element/description/


class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        dict1 = {}
        n = len(nums)
        i = 0
        while i < n:
            tmp = dict1.get(nums[i], 0)
            if tmp == 0:
                dict1[nums[i]] = 1
            else:
                dict1[nums[i]] = tmp + 1
            i += 1

        dict_len = len(dict1)
        keys = list(dict1.keys())
        values = list(dict1.values())
        i = 0
        while i < dict_len:
            if values[i] > n / 2:
                return keys[i]
            i += 1

        return 0


array1 = [2, 2, 1, 1, 1, 2, 2, 3, 2]
obj = Solution()
ret = obj.majorityElement(array1)
print(array1)
print("majorityElement = ", ret)
