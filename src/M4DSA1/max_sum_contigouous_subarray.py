class Soluton:
    def max_sum(self, arr):
        max_so_far, max_sum = 0, float('-inf')

        for num in arr:
            max_so_far += num
            max_sum = max(max_so_far, max_sum)
            if max_so_far < 0: max_so_far = 0

        return max_sum
    
solution = Soluton()

print(solution.max_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]))