def solution():
    total_time = 24*60  # total minutes in a day
    tv_time = (1/5) * total_time  # minutes spent watching TV
    studying_time = (3/4) * (total_time - tv_time)  # minutes spent studying after subtracting TV time
    result = studying_time
    return result

print(solution())