def solution():
    # Define the number of calls per day
    calls_monday = 35
    calls_tuesday = 46
    calls_wednesday = 27
    calls_thursday = 61
    calls_friday = 31

    # Calculate the total number of calls
    total_calls = calls_monday + calls_tuesday + calls_wednesday + calls_thursday + calls_friday

    # Calculate the average number of calls per day
    average_calls = total_calls / 5
    result = average_calls
    return result

print(solution())