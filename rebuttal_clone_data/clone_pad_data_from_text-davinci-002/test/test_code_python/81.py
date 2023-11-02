def solution():
    
    green_crayons = 5
    blue_crayons = 8
    total_crayons = green_crayons + blue_crayons
    given_out_green = 3
    given_out_blue = 1
    crayons_left = total_crayons - (given_out_green + given_out_blue)
    result = crayons_left
    
    return result

print(solution())