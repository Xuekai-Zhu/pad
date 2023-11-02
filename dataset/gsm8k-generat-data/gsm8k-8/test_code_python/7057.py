def solution():
    # Define the number of green and red flowers
    green_flowers = 9
    red_flowers = 3 * green_flowers

    # Calculate the number of blue flowers
    blue_flowers = 0.5 * 96

    # Calculate the total number of yellow flowers
    total_flowers = green_flowers + red_flowers + blue_flowers + yellow_flowers
    yellow_flowers = 96 - total_flowers

    result = yellow_flowers
    return result

print(solution())