def solution():
    # Calculate the total number of flowers in the garden
    total_flowers = 6 * 13

    # Calculate the total number of yellow and green flowers
    yellow_flowers = 12
    green_flowers = 2 * yellow_flowers

    # Calculate the total number of red flowers
    red_flowers = total_flowers - yellow_flowers - green_flowers
    result = red_flowers
    return result

print(solution())