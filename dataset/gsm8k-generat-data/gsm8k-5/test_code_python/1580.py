def solution():
    # Calculate the total number of flowers in the garden
    total_flowers = 6 * 13

    # Calculate the number of green flowers
    num_green_flowers = 12 * 2

    # Calculate the total number of non-red flowers
    non_red_flowers = 12 + num_green_flowers

    # Calculate the number of red flowers
    num_red_flowers = total_flowers - non_red_flowers

    result = num_red_flowers
    return result

print(solution())