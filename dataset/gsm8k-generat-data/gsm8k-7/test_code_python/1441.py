def solution():
    num_classes_per_week = 3
    num_minutes_per_class = 90
    calories_burned_per_minute = 7

    # Calculate the total number of minutes James spends spinning per week
    total_minutes_per_week = num_classes_per_week * num_minutes_per_class

    # Calculate the total number of calories James burns spinning per week
    total_calories_burned_per_week = total_minutes_per_week * calories_burned_per_minute
    result = total_calories_burned_per_week
    return result

print(solution())