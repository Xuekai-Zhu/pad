def solution():
    
    baths_per_week = 2
    showers_per_week = 1
    total_cleanings_per_week = baths_per_week + showers_per_week
    weeks_per_year = 52
    total_cleanings_per_year = total_cleanings_per_week * weeks_per_year
    result = total_cleanings_per_year
    return result

print(solution())