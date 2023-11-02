def solution():
    spinning_frequency = 3  # James takes a spinning class 3 times a week
    time_per_class = 1.5  # James works out for 1.5 hours each class
    calories_per_minute = 7  # James burns 7 calories per minute

    # Calculate the total number of minutes James spends in spinning classes per week
    total_minutes = spinning_frequency * time_per_class * 60

    # Calculate the total number of calories James burns per week
    total_calories = total_minutes * calories_per_minute
    result = total_calories
    return result

print(solution())