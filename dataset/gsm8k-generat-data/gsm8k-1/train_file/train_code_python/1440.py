def solution():
    """James takes a spinning class 3 times a week. He works out for 1.5 hours each class and burns 7 calories per minute. How many calories does he burn per week?"""
    classes_per_week = 3
    workout_duration = 1.5  # hours
    cal_per_minute = 7
    total_calories = classes_per_week * workout_duration * 60 * cal_per_minute
    result = total_calories
    return result

print(solution())