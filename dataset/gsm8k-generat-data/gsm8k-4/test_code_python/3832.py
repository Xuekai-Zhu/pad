def solution():
    """A florist is making bouquets for the weekend. The florist uses red, yellow, orange, and purple flowers, and each bouquet contains 9 flowers of any color combinations. This week he planted 125 seeds for each color of flower. Unfortunately, a fungus killed 45 red flowers, 61 yellow, 30 orange, and 40 purple flowers. How many bouquets can the florist make this weekend?"""
    # Define the number of seeds planted for each color
    RED_SEEDS = 125
    YELLOW_SEEDS = 125
    ORANGE_SEEDS = 125
    PURPLE_SEEDS = 125

    # Define the number of flowers lost to the fungus for each color
    RED_LOST = 45
    YELLOW_LOST = 61
    ORANGE_LOST = 30
    PURPLE_LOST = 40

    # Calculate the number of flowers available for each color
    red_flowers = RED_SEEDS - RED_LOST
    yellow_flowers = YELLOW_SEEDS - YELLOW_LOST
    orange_flowers = ORANGE_SEEDS - ORANGE_LOST
    purple_flowers = PURPLE_SEEDS - PURPLE_LOST

    # Calculate the maximum number of bouquets that can be made
    max_bouquets = min(red_flowers, yellow_flowers, orange_flowers, purple_flowers) // 9

    # Return the result
    result = max_bouquets
    return result

print(solution())