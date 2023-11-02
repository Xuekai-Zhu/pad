def solution():
    
    hours_per_week = 48
    courses_per_week = 4
    total_hours = hours_per_week * 4
    hourly_rate = 25
    earnings_per_course = total_hours / courses_per_week * hourly_rate
    result = earnings_per_course
    return result

print(solution())