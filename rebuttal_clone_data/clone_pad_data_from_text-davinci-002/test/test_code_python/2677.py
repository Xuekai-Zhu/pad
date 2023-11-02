def solution():
    total_miles = 3
    calories_per_mile = 150
    calories_consumed = 200
    total_calories_burned = total_miles * calories_per_mile
    net_calorie_deficit = total_calories_burned - calories_consumed
    result = net_calorie_deficit
    
    return result

print(solution())