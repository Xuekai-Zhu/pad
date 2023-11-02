def solution():
    
    water_amount = 122
    total_filled = 6 * 5 + 4 * 8
    remaining_water = water_amount - total_filled
    four_oz_glasses = remaining_water // 4
    result = four_oz_glasses
    return result

print(solution())