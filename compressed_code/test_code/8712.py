def solution():
    
    caps_per_minute_A = 12
    caps_per_minute_B = caps_per_minute_A - 2
    caps_per_minute_C = caps_per_minute_B + 5
    total_caps_per_minute = caps_per_minute_A + caps_per_minute_B + caps_per_minute_C
    total_caps_in_10_min = total_caps_per_minute * 10
    result = total_caps_in_10_min
    return result

print(solution())