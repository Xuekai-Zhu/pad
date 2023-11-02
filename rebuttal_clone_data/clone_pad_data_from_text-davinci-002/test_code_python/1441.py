def solution():
    classes_per_week = 3
    minutes_per_class = 90
    calories_per_minute = 7
    calories_burned_per_week = classes_per_week * minutes_per_class * calories_per_minute
    result = calories_burned_per_week
    return result

print(solution())