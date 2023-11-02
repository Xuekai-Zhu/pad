def solution():
    turkeys_roasted = 2
    turkey_weight = 16
    minutes_per_pound = 15
    total_minutes = turkey_weight * minutes_per_pound
    total_hours = total_minutes / 60
    expected_time = 6
    start_time = expected_time - total_hours
    result = start_time
    return result

print(solution())