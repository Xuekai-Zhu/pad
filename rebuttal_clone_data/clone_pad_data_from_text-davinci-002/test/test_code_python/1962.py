def solution():
    minutes_without_brother = 9
    minutes_with_brother = 12
    minutes_per_mile = minutes_with_brother - minutes_without_brother
    miles = 20
    total_time = minutes_per_mile * miles
    result = total_time
    return result

print(solution())