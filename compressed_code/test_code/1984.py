def solution():
    
    glasses_per_day = 4
    ounces_per_glass = 5
    ounces_per_bottle = 35
    glasses_per_bottle = ounces_per_bottle / ounces_per_glass
    bottles_per_day = glasses_per_day / glasses_per_bottle
    bottles_per_week = bottles_per_day * 7
    result = bottles_per_week
    return result

print(solution())