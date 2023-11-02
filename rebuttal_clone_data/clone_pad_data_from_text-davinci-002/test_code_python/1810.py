def solution():
     capsules_100mg = 100
     capsules_500mg = 500
     cost_100mg = 5
     cost_500mg = 2
     total_capsules = capsules_100mg + capsules_500mg
     total_cost = cost_100mg + cost_500mg
     result = total_capsules / total_cost
     return result

print(solution())