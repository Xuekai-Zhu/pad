def solution():
    total_hours = 7.5
    total_minutes = total_hours * 60
    minutes_practiced_2_days = 86 * 2
    minutes_practiced_other_days = total_minutes - minutes_practiced_2_days
    result = minutes_practiced_other_days
    return result

print(solution())