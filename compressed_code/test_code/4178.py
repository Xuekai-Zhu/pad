def solution():
    
    day1_minutes = 2 * 60
    day2_minutes = 2 * day1_minutes
    day3_minutes = day2_minutes - 60
    total_minutes = day1_minutes + day2_minutes + day3_minutes
    result = total_minutes
    return result

print(solution())