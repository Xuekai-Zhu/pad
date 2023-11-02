def solution():
    
    apple_speed = 3
    mac_speed = 4
    distance = 24
    apple_time = distance / apple_speed
    mac_time = distance / mac_speed
    time_difference = apple_time - mac_time
    minutes_difference = time_difference * 60
    result = minutes_difference
    return result

print(solution())