def solution():
     initial_cost = 10
     food_weeks = 3
     food_daily = 1/3
     food_bag = 3.5
     food_cost = 2
     total_cost = initial_cost + (food_weeks * food_daily * food_cost)
     result = total_cost
     return result

print(solution())