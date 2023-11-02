def solution():
    
    sqft_wall_1 = 5 * 8
    sqft_wall_2 = 7 * 8
    total_sqft = sqft_wall_1 + sqft_wall_2
    tiles_per_sqft = 4
    turquoise_price = 13
    purple_price = 11
    turquoise_tiles_needed = total_sqft * tiles_per_sqft
    purple_tiles_needed = turquoise_tiles_needed
    turquoise_cost = turquoise_tiles_needed * turquoise_price
    purple_cost = purple_tiles_needed * purple_price
    savings = turquoise_cost - purple_cost
    result = savings
    return result

print(solution())