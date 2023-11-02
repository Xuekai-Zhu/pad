def solution():
    """A florist is making bouquets for the weekend. The florist uses red, yellow, orange, and purple flowers, and each bouquet contains 9 flowers of any color combinations. This week he planted 125 seeds for each color of flower. Unfortunately, a fungus killed 45 red flowers, 61 yellow, 30 orange, and 40 purple flowers. How many bouquets can the florist make this weekend?"""
    # Define the number of seeds of each color planted
    red_seeds = 125
    yellow_seeds = 125
    orange_seeds = 125
    purple_seeds = 125

    # Define the number of flowers of each color killed by the fungus
    red_killed = 45
    yellow_killed = 61
    orange_killed = 30
    purple_killed = 40

    # Calculate the number of flowers of each color remaining
    red_remaining = red_seeds - red_killed
    yellow_remaining = yellow_seeds - yellow_killed
    orange_remaining = orange_seeds - orange_killed
    purple_remaining = purple_seeds - purple_killed

    # Calculate the number of bouquets the florist can make
    bouquets = min(red_remaining, yellow_remaining, orange_remaining, purple_remaining) // 9

    # Display the number of bouquets
    result = bouquets
    return result

print(solution())