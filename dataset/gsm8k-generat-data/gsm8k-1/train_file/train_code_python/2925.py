def solution():
    """Apple can run at a rate of 3 miles per hour. Mac can run at a rate of 4 miles per hour. In minutes, how much faster will Mac run a 24 mile race?"""
    apple_speed = 3
    mac_speed = 4
    distance = 24
    apple_time = distance / apple_speed
    mac_time = distance / mac_speed
    time_difference = apple_time - mac_time
    time_difference_minutes = time_difference * 60
    result = time_difference_minutes
    return result

print(solution())