def solution():
    
    ny_to_chicago_time = 4
    chicago_to_miami_time = ny_to_chicago_time * 3
    total_travel_time = ny_to_chicago_time + 1 + chicago_to_miami_time
    result = total_travel_time
    return result

print(solution())