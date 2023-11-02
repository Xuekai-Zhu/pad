def solution():
    
    total_crayons = 24
    red_crayons = 8
    blue_crayons = 6
    green_crayons = (2/3) * blue_crayons
    pink_crayons = total_crayons - red_crayons - blue_crayons - green_crayons
    result = pink_crayons
    return result

print(solution())