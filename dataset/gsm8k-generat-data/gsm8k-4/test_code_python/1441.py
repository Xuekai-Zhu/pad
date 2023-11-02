def solution():
    """James takes a spinning class 3 times a week. He works out for 1.5 hours each class and burns 7 calories per minute. How many calories does he burn per week?"""
    # Define the number of spinning classes per week and the duration of each class
    classes_per_week = 3
    class_duration = 1.5  # hours

    # Define the number of minutes in an hour
    MINUTES_PER_HOUR = 60

    # Define the number of calories burned per minute
    CALORIES_PER_MINUTE = 7

    # Calculate the number of minutes per class and the total number of minutes per week
    minutes_per_class = class_duration * MINUTES_PER_HOUR
    total_minutes_per_week = classes_per_week * minutes_per_class

    # Calculate the total number of calories burned per week
    total_calories_burned = total_minutes_per_week * CALORIES_PER_MINUTE

    # Return the result
    result = total_calories_burned
    return result

print(solution())