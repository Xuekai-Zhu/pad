def solution():
     shirts_bought = 5
     cost_15 = 15
     cost_20 = 20
     shirts_15 = 3
     shirts_20 = shirts_bought - shirts_15
     total_15 = cost_15 * shirts_15
     total_20 = cost_20 * shirts_20
     cost_of_all_shirts = total_15 + total_20
     result = cost_of_all_shirts
 
     return result

print(solution())