def solution():
    
    avg_temp = 60
    total_temp = avg_temp * 7 
    temp_first_three_days = 40 * 3
    temp_thursday_friday = 80 * 2
    temp_remaining_days = total_temp - temp_first_three_days - temp_thursday_friday
    result = temp_remaining_days
    return result

print(solution())