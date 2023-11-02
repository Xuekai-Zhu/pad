def solution():
     total_cost = 1500
     t_shirt_cost = 100
     t_shirt_quantity = 5
     total_cost_of_t_shirts = t_shirt_cost * t_shirt_quantity
     pants_cost = total_cost - total_cost_of_t_shirts
     pants_quantity = 4
     cost_per_pair_of_pants = pants_cost / pants_quantity
     result = cost_per_pair_of_pants
     return result

print(solution())