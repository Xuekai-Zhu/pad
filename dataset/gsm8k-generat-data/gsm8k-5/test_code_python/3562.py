def solution():
    total_stamps = 930  # The boys have 930 stamps all together

    # Set up the equations for the number of stamps each boy has
    # Let x be the number of stamps AJ has
    # Then KJ has x/2 stamps and CJ has 5 + 2(x/2) = 5 + x stamps
    # The total number of stamps is x + x/2 + 5 + x = 930
    # Simplifying, we get 5x/2 = 925, so x = 370

    stamps_aj = 370  # AJ has 370 stamps
    result = stamps_aj
    return result

print(solution())