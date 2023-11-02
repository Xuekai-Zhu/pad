def solution():
     ounces_per_glass = 5
     ounces_per_bottle = 35
     glasses_per_day = 4
     glasses_per_week = glasses_per_day * 7
     bottles_per_week = glasses_per_week / ounces_per_bottle
     result = bottles_per_week
     return result

print(solution())