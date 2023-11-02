def solution():
    times_per_week = 3  # James takes a spinning class 3 times a week
    time_per_class = 1.5  # He works out for 1.5 hours each class
    calories_per_minute = 7  # He burns 7 calories per minute

    # Calculate the total number of calories James burns per week
    total_minutes = times_per_week * time_per_class * 60  # Convert hours to minutes and multiply by the number of classes per week
    total_calories = total_minutes * calories_per_minute
    result = total_calories
    return result

print(solution())