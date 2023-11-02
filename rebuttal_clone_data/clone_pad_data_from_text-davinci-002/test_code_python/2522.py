def solution():
     cost_large = 15
     cost_small = (23 - cost_large) / 1
     cost_3small = cost_small * 3
     total_cost = cost_large + cost_3small
     result = total_cost
     return result

print(solution())