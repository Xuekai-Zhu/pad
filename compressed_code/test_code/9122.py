def solution():
    
    water_amount = 122
    used_amount = (6 * 5) + (4 * 8)
    remaining_water = water_amount - used_amount
    glasses_4_ounces = remaining_water // 4
    result = glasses_4_ounces
    return result

print(solution())