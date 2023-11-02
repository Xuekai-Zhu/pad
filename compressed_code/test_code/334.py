def solution():
    
    roberto_skips_per_min = 4200 / 60
    valerie_skips_per_min = 80
    total_mins = 15
    roberto_skips = roberto_skips_per_min * total_mins
    valerie_skips = valerie_skips_per_min * total_mins
    total_skips = roberto_skips + valerie_skips
    result = total_skips
    return result

print(solution())