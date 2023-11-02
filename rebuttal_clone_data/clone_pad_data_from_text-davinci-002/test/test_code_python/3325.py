def solution():
     total_budget = 260
     cost_of_clothes = 18.50 + 18.50 + 63
     remaining_budget = total_budget - cost_of_clothes
     cost_per_item = remaining_budget / 4
     result = cost_per_item
     return result

print(solution())