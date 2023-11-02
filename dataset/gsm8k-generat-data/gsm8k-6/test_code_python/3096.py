def solution():
    # Calculate the total number of 2-hour intervals from 3 AM to 11 AM
    num_intervals = (11 - 3) // 2

    # Calculate the total increase in temperature in those intervals
    temp_increase = num_intervals * 1.5

    # Calculate the temperature at 11 AM
    temp_at_11AM = 50 + temp_increase

    result = temp_at_11AM
    return result

print(solution())