def solution():
    """Alvin owns coconut trees that yield 5 coconuts each. If a coconut can be sold for $3 and Alvin needs $90, how many coconut trees does he have to harvest?"""
    # Define the yield and selling price of a coconut
    COCONUT_YIELD = 5
    COCONUT_PRICE = 3

    # Define the amount of money Alvin needs and calculate the number of coconuts he needs to sell
    needed_cash = 90
    total_coconuts_needed = needed_cash / COCONUT_PRICE

    # Calculate the number of coconut trees Alvin needs to harvest
    trees_needed = total_coconuts_needed / COCONUT_YIELD

    # Round up to the nearest whole number of trees
    trees_needed = math.ceil(trees_needed)

    # Display the number of trees needed
    result = trees_needed
    return result

print(solution())