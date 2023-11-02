def solution():
    
    initial_green_crayons = 5
    initial_blue_crayons = 8
    green_crayons_given = 3
    blue_crayons_given = 1
    remaining_green_crayons = initial_green_crayons - green_crayons_given
    remaining_blue_crayons = initial_blue_crayons - blue_crayons_given
    total_crayons_left = remaining_green_crayons + remaining_blue_crayons
    result = total_crayons_left
    return result

print(solution())