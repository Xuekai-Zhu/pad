def solution():
    
    soccer_hours_per_day = 2
    band_hours_per_day = 1.5
    soccer_days = 3
    band_days = 2
    total_soccer_hours = soccer_hours_per_day * soccer_days
    total_band_hours = band_hours_per_day * band_days
    total_hours = total_soccer_hours + total_band_hours
    result = total_hours
    return result

print(solution())