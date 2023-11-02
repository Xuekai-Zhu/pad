def solution():
    avg_temp_week = 60 # Given average temperature for the week
    temp_first_3_days = 40 # Temperature on first three days
    temp_thurs_fri = 80 # Temperature on Thursday and Friday
    total_temp_first5 = temp_first_3_days * 3 + temp_thurs_fri * 2 # Total temperature for the first 5 days
    remaining_days = 7 - 5 # Remaining days in the week
    total_remaining_temp = avg_temp_week * remaining_days - total_temp_first5 # Calculate the total temperature for remaining days
    result = total_remaining_temp
    return result

print(solution())