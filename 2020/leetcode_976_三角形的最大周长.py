from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A = sorted(A,reverse=True)
        print(A)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return A[i]+A[i+1]+A[i+2]
        return 0

input1 = [[2,1,2], [1,2,1], [3,2,3,4], [3,6,2,3]]
for A in input1:
    test = Solution()
    print(test.largestPerimeter(A))