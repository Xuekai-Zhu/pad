def solution():
     cans_of_soda = 5
     ounces_per_can = 12
     total_ounces_of_soda = cans_of_soda * ounces_per_can
     ounces_of_water = 64
     total_fluid_ounces = total_ounces_of_soda + ounces_of_water
     fluid_ounces_per_day = total_fluid_ounces
     fluid_ounces_per_week = fluid_ounces_per_day * 7
     result = fluid_ounces_per_week
     return result

print(solution())