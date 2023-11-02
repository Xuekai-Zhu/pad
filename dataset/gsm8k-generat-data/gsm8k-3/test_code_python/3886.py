def solution():
    """Rebecca bought 22 items for her camping trip, including tent stakes, packets of drink mix, and bottles of water.  She bought 3 times as many packets of drink mix as tent stakes.  She also bought 2 more bottles of water than she did tent stakes.  How many tent stakes did she buy?"""
    # Let's define some variables
    tent_stakes = x
    drink_mix = 3*x
    water_bottles = x+2

    # We know that the total number of items is 22
    total_items = tent_stakes + drink_mix + water_bottles

    # Therefore
    x = (22-2)/4

    result = x
    return result

print(solution())