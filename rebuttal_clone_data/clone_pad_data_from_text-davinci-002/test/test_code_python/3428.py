def solution():
     joy_pencils = 30
     colleen_pencils = 50
     price_per_pencil = 4
     total_joy_cost = joy_pencils * price_per_pencil
     total_colleen_cost = colleen_pencils * price_per_pencil
     diff_in_cost = total_colleen_cost - total_joy_cost
     result = diff_in_cost
     return result

print(solution())