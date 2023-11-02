def solution():
    
    naps_per_week = 3
    nap_duration = 2
    days = 70
    total_nap_hours = naps_per_week * nap_duration * (days/7)
    result = total_nap_hours
    return result

print(solution())