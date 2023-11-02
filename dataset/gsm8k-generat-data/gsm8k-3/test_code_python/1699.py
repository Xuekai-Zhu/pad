def solution():
    """A garden is filled with 105 flowers of various colors. There are twice as many red flowers as orange. There are five fewer yellow flowers than red. If there are 10 orange flowers, how many pink and purple flowers are there if they have the same amount and there are no other colors?"""
    # Define the number of orange flowers
    orange_flowers = 10

    # Calculate the number of red flowers
    red_flowers = 2 * orange_flowers

    # Calculate the number of yellow flowers
    yellow_flowers = red_flowers - 5

    # Calculate the total number of pink and purple flowers
    pink_purple_flowers = 105 - orange_flowers - red_flowers - yellow_flowers

    # Divide the number of pink and purple flowers in half, since they have the same amount
    pink_flowers = purple_flowers = pink_purple_flowers / 2

    # Display the number of pink and purple flowers
    result = pink_flowers + purple_flowers
    return result

print(solution())