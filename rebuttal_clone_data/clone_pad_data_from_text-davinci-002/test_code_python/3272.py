def solution():
    old_toilet_use = 5
    new_toilet_use = old_toilet_use * 0.8
    flushes_per_day = 15
    days_in_month = 30
    total_flushes = flushes_per_day * days_in_month
    old_toilet_gallons = old_toilet_use * total_flushes
    new_toilet_gallons = new_toilet_use * total_flushes
    gallons_saved = old_toilet_gallons - new_toilet_gallons
    result = gallons_saved
    
    return result

print(solution())