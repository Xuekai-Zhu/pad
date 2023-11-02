def solution():
    """The average temperature in Orlando in a particular week was 60 degrees. If the temperature on each of the first 3 days in that week was 40, and the temperature for Thursday and Friday was 80 degrees each, calculate the total temperature of the remaining days of that week."""
    # Calculate the total temperature for the first 3 days
    temp_first_3_days = 40 * 3

    # Calculate the total temperature for Thursday and Friday
    temp_thursday_friday= 80 * 2

    # Calculate the total temperature for the entire week
    total_temp = 60 * 7

    # Calculate the total temperature for the remaining days of the week
    remaining_temp = total_temp - temp_first_3_days - temp_thursday_friday

    # Display the remaining temperature
    result = remaining_temp
    return result

print(solution())