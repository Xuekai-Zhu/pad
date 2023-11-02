def solution():
    
    total_students = 80
    half_day_percent = 0.25
    half_day_students = total_students * half_day_percent
    full_day_students = total_students - half_day_students
    result = full_day_students
    return result

print(solution())