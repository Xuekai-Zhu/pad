def solution():
    """Alvin owns coconut trees that yield 5 coconuts each. If a coconut can be sold for $3 and Alvin needs $90, how many coconut trees does he have to harvest?"""
    # Define the price of a coconut and the amount of money Alvin needs
    COCONUT_PRICE = 3
    TOTAL_MONEY_NEEDED = 90

    # Calculate the number of coconuts Alvin needs to sell
    coconuts_needed = TOTAL_MONEY_NEEDED // COCONUT_PRICE

    # Calculate the number of coconut trees Alvin needs to harvest
    trees_needed = coconuts_needed // 5

    # If there are not enough coconuts from one tree, add one more tree
    if coconuts_needed % 5 != 0:
        trees_needed += 1

    # return the result
    result = trees_needed
    return result

print(solution())