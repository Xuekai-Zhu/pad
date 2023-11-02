def solution():
    # Calculate the total temperature of the first 3 days
    temp_first_3_days = 40*3
 
    # Calculate the total temperature of Thursday and Friday
    temp_last_2_days = 80 * 2

    # Calculate the total temperature of the remaining days
    total_temp_remaining_days = (60*7) - temp_first_3_days - temp_last_2_days
 
    result = total_temp_remaining_days
    return result

print(solution())