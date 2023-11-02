def solution():
    """A crayon box has 24 crayons total.  8 crayons are red, 6 crayons are blue, there are 2/3 the number of green crayons as blue crayons, and the rest of the crayons are pink.  How many crayons are pink?"""
    # Define the total number of crayons and the number of red and blue crayons
    total_crayons = 24
    red_crayons = 8
    blue_crayons = 6

    # Calculate the number of green crayons
    green_crayons = (2/3) * blue_crayons

    # Calculate the number of pink crayons
    pink_crayons = total_crayons - red_crayons - blue_crayons - green_crayons

    # return the result
    result = pink_crayons
    return result

print(solution())