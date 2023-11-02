def solution():
    breakfast_calories = 900
    jogging_calories = 10
    minutes_jogging = 30
    total_calories = breakfast_calories - (jogging_calories * minutes_jogging)
    result = total_calories
    return result

print(solution())