def solution():
    """Samantha bought a crate of 30 eggs for $5. If she decides to sell each egg for 20 cents, how many eggs will she have left by the time she recovers her capital from the sales?"""
    # Define the initial cost of the eggs and the selling price per egg
    INITIAL_COST = 5
    SELLING_PRICE = 0.2

    # Calculate the number of eggs that need to be sold to recover the initial cost
    eggs_to_sell = INITIAL_COST / SELLING_PRICE

    # Calculate the number of eggs left after selling the required number to recover the cost
    eggs_left = 30 - eggs_to_sell

    # Return the result
    result = eggs_left
    return result

print(solution())