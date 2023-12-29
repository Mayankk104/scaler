class Solution:
    def colsest_min_max(self, arr):
        min_val, max_val, min_ptr, max_ptr, min_distance = float('inf'), float('-inf'), -1, -1, float('inf')

        for num in arr:
            min_val = min(min_val, num)
            max_val = max(max_val, num)

        for i in range(len(arr)):
            if arr[i] == min_val: min_ptr = i
            if arr[i] == max_val: max_ptr = i
            if min_ptr != -1 and max_ptr != -1: min_distance = min(min_distance, abs(max_ptr-min_ptr))

        return min_distance + 1
    
solution = Solution()
min_distance = solution.colsest_min_max([814,761,697,483,981])
print(min_distance)