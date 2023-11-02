def solution():
    # Calculate the number of green crayons
    blue_crayons = 6
    green_crayons = (2/3) * blue_crayons

    # Calculate the total number of red, blue, and green crayons
    total_red_blue_green = red_crayons + blue_crayons + green_crayons

    # Calculate the number of pink crayons
    pink_crayons = 24 - total_red_blue_green

    return pink_crayons

print(solution())