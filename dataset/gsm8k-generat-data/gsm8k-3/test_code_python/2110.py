def solution():
    """In a grocery store, Julia bought 2 pieces of Snickers and 3 packs of M&M's. If each piece of Snickers costs $1.5 and a pack of M&M's has the same cost as 2 Snickers, how much is Julia's change if she gave the cashier 2 $10 bills?"""
    # Define the cost of each piece of Snickers and pack of M&M's
    SNICKERS_PRICE = 1.5
    MM_PRICE = SNICKERS_PRICE * 2

    # Calculate the total cost of the Snickers
    snickers_cost = 2 * SNICKERS_PRICE

    # Calculate the total cost of the M&M's
    mm_cost = 3 * MM_PRICE

    # Calculate the total cost of all the items
    total_cost = snickers_cost + mm_cost

    # Calculate the amount of change
    change = (10 * 2) - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())