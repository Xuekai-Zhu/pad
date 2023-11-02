def solution():
    
    red_tulips_per_row = 6
    blue_tulips_per_row = 8
    red_tulips_bought = 36
    blue_tulips_bought = 24
    total_red_tulips = red_tulips_bought * red_tulips_per_row
    total_blue_tulips = blue_tulips_bought * blue_tulips_per_row
    total_rows = total_red_tulips + total_blue_tulips
    result = total_rows
    return result

print(solution())