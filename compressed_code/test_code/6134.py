def solution():
    
    roberto_skips_per_minute = 4200 / 60
    valerie_skips_per_minute = 80
    total_skips_per_minute = roberto_skips_per_minute + valerie_skips_per_minute
    total_skips = total_skips_per_minute * 15
    result = total_skips
    return result

print(solution())