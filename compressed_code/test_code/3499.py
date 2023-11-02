def solution():
    
    naps_per_week = 3
    nap_length = 2
    total_days = 70
    total_nap_hours = naps_per_week * nap_length * (total_days // 7)
    result = total_nap_hours
    return result

print(solution())