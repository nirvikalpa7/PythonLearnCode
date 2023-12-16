
# 242. Valid Anagram
# https://leetcode.com/problems/valid-anagram/description/

class Solution:

    def getDict(self, s: str):
        dict1 = {}
        len1 = len(s)
        i = 0
        while i < len1:
            tmp = dict1.get(s[i], 0)
            if tmp == 0:
                dict1[s[i]] = 1
            else:
                dict1[s[i]] = tmp + 1
            i += 1
        return dict1

    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = self.getDict(s)
        dict2 = self.getDict(t)
        return dict1 == dict2


str1 = "anagram"
print(str1)
str2 = "gamanar"
print(str2)
check = Solution()
print(check.isAnagram(str1, str2))

str3 = "mama papa"
print(str3)
str4 = "nama pana"
print(str4)
print(check.isAnagram(str3, str4))
