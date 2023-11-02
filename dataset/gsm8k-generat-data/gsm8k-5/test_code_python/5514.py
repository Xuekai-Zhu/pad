def solution():
    total_cans = 24  # The cooler is filled with 24 cans of soda
    ratio_orange_pop = 2  # There are twice as many cans of orange pop as cherry soda

    # Use algebra to solve for the number of cans of cherry soda
    # Let x be the number of cans of cherry soda, then the number of cans of orange pop is 2x
    # Total number of cans = number of cherry soda + number of orange pop = x + 2x = 3x
    # So 3x = total number of cans = 24, therefore x = 8
    cans_cherry_soda = 8

    result = cans_cherry_soda
    return result

print(solution())