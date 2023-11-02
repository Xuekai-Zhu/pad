def solution():
    minutes_per_lawn = 30
    lawns_cut = 8
    minutes_spent_cutting = minutes_per_lawn * lawns_cut
    hours_spent_cutting = minutes_spent_cutting / 60
    result = hours_spent_cutting
    
    return result

print(solution())