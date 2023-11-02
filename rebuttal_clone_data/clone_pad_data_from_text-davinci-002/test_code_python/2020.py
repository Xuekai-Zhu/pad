def solution():
    oysters_per_minute = 10
    minutes_per_hour = 60
    hours = 2
    oysters_per_hour = oysters_per_minute * minutes_per_hour
    total_oysters = oysters_per_hour * hours
    result = total_oysters
    return result

print(solution())