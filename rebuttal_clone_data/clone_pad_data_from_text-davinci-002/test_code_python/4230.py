def solution():
     ounces_of_water = 122
     5_ounce_glasses = 6
     8_ounce_glasses = 4
     ounces_used = (5_ounce_glasses * 5) + (8_ounce_glasses * 8)
     remaining_water = ounces_of_water - ounces_used
     4_ounce_glasses = remaining_water / 4
     result = 4_ounce_glasses 
     return result

print(solution())