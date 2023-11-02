def solution():
    # Define the number of red and blue crayons
    red_crayons = 8
    blue_crayons = 6

    # Calculate the number of green crayons
    green_crayons = 2/3 * blue_crayons

    # Calculate the total number of non-pink crayons
    non_pink_crayons = red_crayons + blue_crayons + green_crayons

    # Calculate the number of pink crayons
    pink_crayons = 24 - non_pink_crayons
    result = pink_crayons
    return result

print(solution())