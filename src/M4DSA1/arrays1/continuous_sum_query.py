"""
Time Complexity: O(A+B) | Space Complexity: O(1)
"""

class Solution:
    def solve(self, A, B):
        beggers = [0] * A

        for cherity in B:
            print(cherity)
            beggers[cherity[0]-1] += cherity[2]
            if cherity[1] < A: beggers[cherity[1]] -= cherity[2]

        print(beggers)

        for i in range(len(beggers)):
            beggers[i] += beggers[i-1]

        return beggers
    
solution = Solution()
print(solution.solve(5, [[1,2,10],[2,3,20],[2,5,25]]))