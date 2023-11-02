def solution():
    
    calls_monday = 35
    calls_tuesday = 46
    calls_wednesday = 27
    calls_thursday = 61
    calls_friday = 31
    total_calls = calls_monday + calls_tuesday + calls_wednesday + calls_thursday + calls_friday
    days_worked = 5
    average_calls = total_calls / days_worked
    result = average_calls
    return result

print(solution())