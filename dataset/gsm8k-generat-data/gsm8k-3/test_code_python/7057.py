def solution():
    """In a school garden, there are flowers in different colors. In total there are 96 flowers of four colors: green, red, blue, and yellow. There are 9 green flowers and three times more red flowers. Blue flowers make up 50% of the total flower count. How many yellow flowers are there?"""
    # Define the number of green flowers
    green_flowers = 9

    # Calculate the number of red flowers
    red_flowers = 3 * green_flowers

    # Calculate the number of blue flowers
    blue_flowers = (50/100) * 96 - (green_flowers + red_flowers)

    # Calculate the number of yellow flowers
    yellow_flowers = 96 - (green_flowers + red_flowers + blue_flowers)

    # Display the number of yellow flowers
    result = yellow_flowers
    return result

print(solution())