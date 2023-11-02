def solution():
    
    ounces_per_day = 72
    ounces_per_bottle = 84
    fill_per_week = int((ounces_per_day * 7) / ounces_per_bottle)
    result = fill_per_week
    return result

print(solution())