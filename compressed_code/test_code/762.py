def solution():
    
    bowl_size = 10
    bowls_per_minute = 5
    soup_size = 6 * 128
    total_bowls = soup_size / bowl_size
    total_time_minutes = total_bowls / bowls_per_minute
    result = round(total_time_minutes)
    return result

print(solution())