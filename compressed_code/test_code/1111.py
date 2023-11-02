def solution():
    
    classes_per_week = 3
    class_duration = 1.5 * 60  
    calories_per_minute = 7
    total_calories_burned = classes_per_week * class_duration * calories_per_minute
    result = total_calories_burned
    return result

print(solution())