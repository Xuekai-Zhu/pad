def solution():
    """The average temperature in Orlando in a particular week was 60 degrees. If the temperature on each of the first 3 days in that week was 40, and the temperature for Thursday and Friday was 80 degrees each, calculate the total temperature of the remaining days of that week."""
    # Define the total number of days in the week
    total_days = 7

    # Define the average temperature for the week
    avg_temp_week = 60

    # Define the temperatures for the first 3 days and Thursday and Friday
    temp_first_3_days = 40
    temp_thursday_friday = 80

    # Calculate the total temperature for the first 5 days
    total_temp_first_5_days = (temp_first_3_days * 3) + (temp_thursday_friday * 2)

    # Calculate the temperature for the remaining 2 days
    temp_remaining_days = ((avg_temp_week * total_days) - total_temp_first_5_days) / 2

    # Calculate the total temperature for the remaining days
    total_temp_remaining_days = temp_remaining_days * 2

    # Return the result
    result = total_temp_remaining_days
    return result

print(solution())