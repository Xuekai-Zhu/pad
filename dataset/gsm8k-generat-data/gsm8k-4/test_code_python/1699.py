def solution():
    """A garden is filled with 105 flowers of various colors. There are twice as many red flowers as orange. There are five fewer yellow flowers than red. If there are 10 orange flowers, how many pink and purple flowers are there if they have the same amount and there are no other colors?"""
    # Define the number of orange flowers and calculate the number of red flowers
    orange_flowers = 10
    red_flowers = 2 * orange_flowers

    # Calculate the number of yellow flowers
    yellow_flowers = red_flowers - 5

    # Calculate the total number of red, orange, and yellow flowers
    total_flowers = red_flowers + orange_flowers + yellow_flowers

    # Calculate the number of pink and purple flowers
    pink_purple_flowers = (105 - total_flowers) / 2

    # return the result
    result = pink_purple_flowers
    return result

print(solution())