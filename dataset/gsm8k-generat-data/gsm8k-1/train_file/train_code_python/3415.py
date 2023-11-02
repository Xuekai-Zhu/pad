def solution():
    """September's temperature fluctuated severely in 1 week. They started off with 40 degrees on Sunday then hit 50 on Monday, 65 on Tuesday, 36 on Wednesday, 82 on Thursday, 72 on Friday and ended the week at 26 on Saturday. What was the average temperature for that week?"""
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