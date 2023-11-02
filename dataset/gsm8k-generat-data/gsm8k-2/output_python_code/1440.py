def solution():
    """James takes a spinning class 3 times a week. He works out for 1.5 hours each class and burns 7 calories per minute. How many calories does he burn per week?"""
    classes_per_week = 3
    class_duration = 1.5 * 60  # in minutes
    calories_per_minute = 7
    total_calories_burned = classes_per_week * class_duration * calories_per_minute
    result = total_calories_burned
    return result

print(solution())