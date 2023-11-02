def solution():
    
    temp_sun = 40
    temp_mon = 50
    temp_tue = 65
    temp_wed = 36
    temp_thu = 82
    temp_fri = 72
    temp_sat = 26
    total_temp = temp_sun + temp_mon + temp_tue + temp_wed + temp_thu + temp_fri + temp_sat
    num_days = 7
    avg_temp = total_temp / num_days
    result = avg_temp
    return result

print(solution())