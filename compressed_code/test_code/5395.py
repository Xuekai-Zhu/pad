def solution():
    
    total_students = 32
    presentation_time = 5
    period_time = 40
    presentations_per_period = period_time // presentation_time
    periods_needed = total_students / presentations_per_period
    result = periods_needed
    return result

print(solution())