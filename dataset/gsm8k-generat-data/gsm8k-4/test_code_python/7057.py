def solution():
    """In a school garden, there are flowers in different colors. In total there are 96 flowers of four colors: green, red, blue, and yellow. There are 9 green flowers and three times more red flowers. Blue flowers make up to 50% of the total flower count. How many yellow flowers are there?"""
    # Define the total number of flowers and the number of green flowers
    total_flowers = 96
    green_flowers = 9

    # Calculate the number of red flowers and the number of blue flowers
    red_flowers = (total_flowers - green_flowers) / 4 * 3
    blue_flowers = total_flowers * 0.5

    # Calculate the number of yellow flowers
    yellow_flowers = total_flowers - green_flowers - red_flowers - blue_flowers

    # return the result
    result = yellow_flowers
    return result

print(solution())