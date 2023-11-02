def solution():
    """John buys 2 packs of gum and 3 candy bars.  Each stick of gum cost half as much as the candy bar.  If the candy bar cost $1.5 each, how much did he pay in total?"""
    # Define the cost of a candy bar
    CANDY_BAR_PRICE = 1.5

    # Calculate the cost of a stick of gum
    GUM_PRICE = CANDY_BAR_PRICE / 2

    # Calculate the total cost of the gum
    gum_cost = 2 * GUM_PRICE

    # Calculate the total cost of the candy bars
    candy_cost = 3 * CANDY_BAR_PRICE

    # Calculate the total cost of John's purchase
    total_cost = gum_cost + candy_cost

    # Display the total cost
    result = total_cost
    return result

print(solution())