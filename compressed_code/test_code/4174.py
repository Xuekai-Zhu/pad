def solution():
    
    ny_to_chicago_time = 4
    chicago_to_miami_time = 3 * ny_to_chicago_time
    total_time = ny_to_chicago_time + 1 + chicago_to_miami_time
    result = total_time
    return result

print(solution())