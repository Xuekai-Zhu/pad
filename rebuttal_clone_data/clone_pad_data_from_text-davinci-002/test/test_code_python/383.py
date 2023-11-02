def solution():
     total_roofing = 300
     free_roofing = 250
     paid_roofing = total_roofing - free_roofing
     cost_per_foot = 8
     total_cost = paid_roofing * cost_per_foot
     result = total_cost
     return result

print(solution())