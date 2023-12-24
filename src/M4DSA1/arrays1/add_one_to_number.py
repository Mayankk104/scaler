class Solution:
    def plus_one(self, arr):
        start, shouldAdd, result = -1, True, []

        for i in range(len(arr)):
            if arr[i] != 0: 
                start = i
                break
        
        if start == -1: return [1]

        for i in range(len(arr) - 1, start - 1, -1):
            if shouldAdd:
                if arr[i] == 9:
                    result.append(0)
                    if start == i: 
                        result.append(i)
                    continue

                result.append(arr[i] + 1)
                shouldAdd = False
                continue
            else:
                result.append(arr[i])

        for i in range(len(arr) // 2):
            result[i], result[len(result) - i - 1] = ( result[len(result) - i - 1], result[i])

        return result
    
solution = Solution()
print(solution.plus_one([2, 5, 6, 8, 6, 1, 2, 4, 5]))