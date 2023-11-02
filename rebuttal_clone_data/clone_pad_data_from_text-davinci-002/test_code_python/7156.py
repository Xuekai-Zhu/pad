def solution():
    miles = 24
    hours = 3
    minutes = 36
    total_time = (hours * 60) + minutes
    time_per_mile = total_time / miles
    result = time_per_mile
    return result

print(solution())