def solution():
     planks_needed = 7
     nails_needed = 20
     cost_of_plank = 3
     cost_of_nail = 0.05
     cost_of_birdhouse = (planks_needed * cost_of_plank) + (nails_needed * cost_of_nail)
     total_cost = cost_of_birdhouse * 4
     result = total_cost
     return result

print(solution())