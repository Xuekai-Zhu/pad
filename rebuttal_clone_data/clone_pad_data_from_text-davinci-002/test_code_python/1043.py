def solution():
     coach_cost = 2500
     sectional_cost = 3500
     other_cost = 2000
     total_cost = coach_cost + sectional_cost + other_cost
     discount = total_cost * .10
     final_cost = total_cost - discount
     result = final_cost
     return result

print(solution())