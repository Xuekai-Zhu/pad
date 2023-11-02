def solution():
    
    mice_per_week = 1/4
    weeks_per_year = 52
    mice_per_year = mice_per_week * weeks_per_year
    mice_per_decade = mice_per_year * 10
    result = mice_per_decade
    return result

print(solution())