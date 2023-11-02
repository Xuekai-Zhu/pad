def solution():
    """There are 14 red crayons, 5 more blue crayons than red crayons, and 6 less yellow crayons than double the blue crayons. How many yellow crayons are there?"""
    red_crayons = 14
    blue_crayons = red_crayons + 5
    yellow_crayons = (2 * blue_crayons) - 6
    result = yellow_crayons
    return result

print(solution())