
# 118. Pascal's Triangle
# https://leetcode.com/problems/pascals-triangle/description/

class Solution:
    def generate(self, numRows: int) :
        ret = []
        line = []

        line.append(1)
        ret.append(list(line))
        if numRows == 1:
            return ret

        line.append(1)
        ret.append(list(line))
        if numRows == 2:
            return ret

        i = 0
        while i < numRows - 2:
            line.clear()
            line.append(1)
            lenRet = len(ret)
            tmpLen = len(ret[lenRet - 1]) - 1
            j = 0
            while True:
                newVal = ret[lenRet - 1][j] + ret[lenRet - 1][j+1]
                line.append(newVal)
                tmpLen -= 1
                j += 1
                if tmpLen == 0:
                    break
            line.append(1)
            ret.append(list(line))
            i += 1

        return ret

obj = Solution()
print(obj.generate(5))