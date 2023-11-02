def solution():
    """Blinky wants to make a three-layer birthday cake for her mom. The recipe for the smallest layer of the cake requires 2 cups of sugar. If the second layer is twice as big as the first and the third layer is three times larger than the second, how many total cups of sugar will she need for the third layer?"""
    # Define the amount of sugar for the smallest layer
    sugar_small = 2

    # Calculate the size of the second layer
    size_second = 2 * 1  # twice as big as the first layer

    # Calculate the size of the third layer
    size_third = 3 * size_second  # three times larger than the second layer

    # Calculate the amount of sugar needed for the third layer
    sugar_third = size_third * sugar_small

    result = sugar_third
    return result

print(solution())