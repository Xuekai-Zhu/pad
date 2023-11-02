def solution():
    """The average temperature in Orlando in a particular week was 60 degrees. If the temperature on each of the first 3 days in that week was 40, and the temperature for Thursday and Friday was 80 degrees each, calculate the total temperature of the remaining days of that week."""
    avg_temp = 60
    total_temp = avg_temp * 7 # total temperature for the week
    temp_first_three_days = 40 * 3
    temp_thursday_friday = 80 * 2
    temp_remaining_days = total_temp - temp_first_three_days - temp_thursday_friday
    result = temp_remaining_days
    return result

print(solution())