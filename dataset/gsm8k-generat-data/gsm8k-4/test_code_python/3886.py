def solution():
    """Rebecca bought 22 items for her camping trip, including tent stakes, packets of drink mix, and bottles of water. She bought 3 times as many packets of drink mix as tent stakes. She also bought 2 more bottles of water than she did tent stakes. How many tent stakes did she buy?"""
    # Define the number of tent stakes and packets of drink mix
    tent_stakes = None
    drink_mix = None

    # Define the total number of items and the number of bottles of water
    total_items = 22
    bottles_of_water = None

    # Set up two equations: drink_mix = 3 * tent_stakes and bottles_of_water = tent_stakes + 2
    # Substitute drink_mix and bottles_of_water in terms of tent_stakes in the equation total_items = tent_stakes + drink_mix + bottles_of_water
    tent_stakes = (total_items - 2) / 4
    drink_mix = 3 * tent_stakes
    bottles_of_water = tent_stakes + 2

    # Return the number of tent stakes
    result = tent_stakes
    return result

print(solution())