def solution():
     calories_per_day = 2500
     calories_on_saturday = 1000
     calories_burned_per_day = 3000
     total_calories = (calories_per_day * 6) + calories_on_saturday
     total_calories_burned = calories_burned_per_day * 7
     kcal_deficit = total_calories_burned - total_calories
     result = kcal_deficit
     return result

print(solution())