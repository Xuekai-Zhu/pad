def solution():
    
    total_calories = 40
    portion_eaten = 3/4
    calories_eaten = total_calories * portion_eaten
    recommended_calories = 25
    calories_above_recommended = calories_eaten - recommended_calories
    result = calories_above_recommended
    return result

print(solution())