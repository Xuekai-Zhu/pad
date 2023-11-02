def solution():
    
    classes_per_week = 3
    workout_duration = 1.5  
    cal_per_minute = 7
    total_calories = classes_per_week * workout_duration * 60 * cal_per_minute
    result = total_calories
    return result

print(solution())