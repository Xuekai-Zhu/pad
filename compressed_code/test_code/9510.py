def solution():
    
    cans_per_day = 5
    ounces_per_can = 12
    ounces_of_soda = cans_per_day * ounces_per_can
    ounces_of_water = 64
    ounces_per_day = ounces_of_soda + ounces_of_water
    days_per_week = 7
    total_fluid_ounces = ounces_per_day * days_per_week
    result = total_fluid_ounces
    return result

print(solution())