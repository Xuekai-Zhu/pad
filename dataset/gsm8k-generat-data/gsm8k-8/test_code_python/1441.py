def solution():
    # Define the variables
    classes_per_week = 3
    duration_per_class = 1.5  # in hours
    calories_per_minute = 7

    # Calculate the total duration of workout per week
    total_duration = classes_per_week * duration_per_class

    # Convert the duration from hours to minutes
    total_duration = total_duration * 60

    # Calculate the total calories burned per week
    total_calories_burned = total_duration * calories_per_minute
    result = total_calories_burned
    return result

print(solution())