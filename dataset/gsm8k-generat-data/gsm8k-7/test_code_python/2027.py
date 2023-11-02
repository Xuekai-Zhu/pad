def solution():
    avg_temp = 60
    temp_first_3_days = 40
    temp_thursday = 80
    temp_friday = 80

    # Calculate the total temperature for the first 3 days
    total_temp_first_3_days = temp_first_3_days * 3

    # Calculate the total temperature for Thursday and Friday
    total_temp_thursday_friday = temp_thursday + temp_friday

    # Calculate the total number of remaining days in the week
    remaining_days = 7 - 3 - 2

    # Calculate the total temperature for the remaining days
    total_temp_remaining = (avg_temp * 7) - total_temp_first_3_days - total_temp_thursday_friday

    result = total_temp_remaining
    return result

print(solution())