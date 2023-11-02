def solution():
    red_crayons = 14
    blue_crayons = red_crayons + 5  # There are 5 more blue crayons than red crayons
    yellow_crayons = 2 * blue_crayons - 6  # There are 6 less yellow crayons than double the blue crayons
    result = yellow_crayons
    return result

print(solution())