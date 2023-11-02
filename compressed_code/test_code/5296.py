def solution():
    
    strings_per_night = 2
    shows_per_week = 6
    weeks = 12
    total_nights = shows_per_week * weeks
    total_strings_broken = strings_per_night * total_nights
    result = total_strings_broken
    return result

print(solution())