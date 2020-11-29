#我自己的解法
class Solution:
    def myAtoi(self, s: str) -> int:
        string = ''
        flag = 0
        for ch in s:
            if ch == ' ' and flag == 0:
                continue
            elif (ch == '-' or ch == '+') and string == '':
                string += ch
            elif ch >= '0' and ch <= '9':
                string += ch
            else:
                break
            flag += 1
        if string in ('', '+', '-'):
            return 0
        else:
            num = int(string)
            if num > 2147483647:
                return 2147483647
            elif num < -2**31:
                return -2147483648
            else:
                return num if num else 0


#最优解
import re
class Solution:
    def myAtoi(self, s: str) -> int:
        return min(max(int(*re.findall(r'^[\+\-]?\d+', s.lstrip())), -2147483648), 2147483647)

test_list = [
    "   -42"
    ,"42"
    ,"4193 with words"
    ,"words and 987"
    ,"-91283472332"
    ,"+342"
    ,'-ed4'
    ,"  0000000000012345678"
]
test_class = Solution()
for s in test_list:
    print(s)
    print(test_class.myAtoi(s))

