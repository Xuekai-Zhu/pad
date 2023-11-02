def solution():
    
    total_teachers = 150
    history_teachers = total_teachers * 0.6
    math_teachers = total_teachers - history_teachers
    sleep_time_per_teacher = 6
    total_sleep_time = math_teachers * sleep_time_per_teacher
    result = total_sleep_time
    return result

print(solution())