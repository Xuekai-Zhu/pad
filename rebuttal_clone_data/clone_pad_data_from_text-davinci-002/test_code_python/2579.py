def solution():
    initial_crayons = 4 * 8
    crayons_to_Mae = 5
    crayons_left = initial_crayons - crayons_to_Mae
    crayons_to_Lea = crayons_left - 15
    result = crayons_to_Lea - crayons_to_Mae
    return result

print(solution())