def solution():
    
    cat1_meows_per_minute = 3
    cat2_meows_per_minute = cat1_meows_per_minute * 2
    cat3_meows_per_minute = cat2_meows_per_minute / 3
    total_meows_per_minute = cat1_meows_per_minute + cat2_meows_per_minute + cat3_meows_per_minute
    minutes = 5
    total_meows = total_meows_per_minute * minutes
    result = total_meows
    return result

print(solution())