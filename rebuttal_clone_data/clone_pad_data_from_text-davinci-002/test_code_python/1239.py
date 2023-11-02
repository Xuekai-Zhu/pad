def solution():
     cost_to_remove = 50
     new_floor_cost = 1.25
     floor_area = 8 * 7
     cost_to_replace = cost_to_remove + (new_floor_cost * floor_area)
     result = cost_to_replace
     
     return result

print(solution())