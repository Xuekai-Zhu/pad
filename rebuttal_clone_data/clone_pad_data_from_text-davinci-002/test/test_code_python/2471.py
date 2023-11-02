def solution():
     total_value = 52
     one_toy_value = 12
     remaining_toys_value = total_value - one_toy_value
     remaining_toys = 8
     cost_per_toy = remaining_toys_value / remaining_toys
     result = cost_per_toy
     return result

print(solution())