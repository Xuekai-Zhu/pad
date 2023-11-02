def solution():
    total_crayons = 24  # The crayon box has 24 crayons in total
    red_crayons = 8
    blue_crayons = 6
    green_crayons = (2/3) * blue_crayons  # The number of green crayons is 2/3 of the number of blue crayons
    # Calculate the number of pink crayons
    pink_crayons = total_crayons - (red_crayons + blue_crayons + green_crayons)
    result = pink_crayons
    return result

print(solution())