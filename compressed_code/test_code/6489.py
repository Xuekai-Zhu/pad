def solution():
    
    cans_per_30min = 30
    minutes_per_hour = 60
    hours = 8
    cans_per_hour = (cans_per_30min * minutes_per_hour) / 30
    total_cans = cans_per_hour * hours
    result = total_cans
    return result

print(solution())