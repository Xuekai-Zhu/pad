def solution():
    total_calories = 40
    recommended_intake = 25
    calories_consumed = total_calories * 0.75
    calories_above_recommended = calories_consumed - recommended_intake
    result = calories_above_recommended
    return result

print(solution())