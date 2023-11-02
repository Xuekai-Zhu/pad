def solution():
    bags_eaten = 3
    ounces_per_bag = 2
    calories_per_ounce = 150
    total_calories = bags_eaten * ounces_per_bag * calories_per_ounce
    minutes_run = 40
    calories_burned = minutes_run * 12
    excess_calories = total_calories - calories_burned
    result = excess_calories
    return result

print(solution())