def solution():
    # Calculate the number of blocks that fell down in the first tower
    fell_down_1 = 7

    # Calculate the height of the second tower
    height_2 = 7 + 5
    # Calculate the number of blocks that fell down in the second tower
    fell_down_2 = height_2 - 2

    # Calculate the height of the final tower
    height_3 = height_2 + 7
    # Calculate the number of blocks that fell down in the final tower
    fell_down_3 = height_3 - 3

    # Calculate the total number of blocks that fell down
    total_fell_down = fell_down_1 + fell_down_2 + fell_down_3
    result = total_fell_down
    return result

print(solution())