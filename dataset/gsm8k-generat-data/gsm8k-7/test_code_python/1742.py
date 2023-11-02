def solution():
    calls_monday = 35
    calls_tuesday = 46
    calls_wednesday = 27
    calls_thursday = 61
    calls_friday = 31

    # Calculate the total number of calls Jean answered in a week
    total_calls = calls_monday + calls_tuesday + calls_wednesday + calls_thursday + calls_friday

    # Calculate the average number of calls Jean answers per day
    average_calls_per_day = total_calls / 5
    result = average_calls_per_day
    return result

print(solution())