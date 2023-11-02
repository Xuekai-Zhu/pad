def solution():
    
    total_attendance = 2700
    first_day_attendance = total_attendance / (1 + 0.5 + 3)
    second_day_attendance = first_day_attendance / 2
    result = second_day_attendance
    return result

print(solution())