class Solution(object):
    def convert(self, s, numRows = 3):
        result = ""
        for i in range(0, numRows):
            increment = numRows + 1
            if i == int(numRows / 2):
                increment = int(increment / 2)
            while i < len(s):
                result += s[i]
                i += increment
        return result

s = Solution()
print(s.convert("PAYPALISHIRING"))
