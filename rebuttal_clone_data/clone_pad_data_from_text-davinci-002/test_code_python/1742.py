def solution():
    calls_answered_monday = 35
    calls_answered_tuesday = 46
    calls_answered_wednesday = 27
    calls_answered_thursday = 61
    calls_answered_friday = 31
    total_calls_answered = calls_answered_monday + calls_answered_tuesday + calls_answered_wednesday + calls_answered_thursday + calls_answered_friday
    average_calls_per_day = total_calls_answered / 5
    result = average_calls_per_day
    return result

print(solution())