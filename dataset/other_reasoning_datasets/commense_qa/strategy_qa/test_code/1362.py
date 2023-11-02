def solution():
    basel_time_zone = "CEST"
    los_angeles_time_zone = "PDT"
    # compare the time difference between Basel and Los Angeles
    if basel_time_zone != los_angeles_time_zone:
        result = "not sure"
    else:
        result = "it depends on the time of day and season"
    return result

print(solution())