def solution():
    
    red_tulips_per_row = 6
    blue_tulips_per_row = 8
    total_red_tulips = 36
    total_blue_tulips = 24
    total_flowers = (total_red_tulips // red_tulips_per_row) + (total_blue_tulips // blue_tulips_per_row)
    result = total_flowers
    return result

print(solution())