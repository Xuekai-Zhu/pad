def solution():
     total_juice_cost = 10
     total_sandwich_cost = 6
     cost_of_one_juice = total_juice_cost / 5
     cost_of_one_sandwich = total_sandwich_cost / 2
     cost_of_one_meal = cost_of_one_juice + cost_of_one_sandwich
     result = cost_of_one_meal
     return result

print(solution())