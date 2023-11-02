def solution():
     cost_per_bale = 15
     new_cost_per_bale = 18
     bales_of_hay = 10
     new_total_cost = new_cost_per_bale * 2 * bales_of_hay
     old_total_cost = cost_per_bale * bales_of_hay
     cost_difference = new_total_cost - old_total_cost
     result = cost_difference
     return result

print(solution())