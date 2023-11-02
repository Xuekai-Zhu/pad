def solution():
    """In a grocery store, Julia bought 2 pieces of Snickers and 3 packs of M&M's. If each piece of Snickers costs $1.5 and a pack of M&M's has the same cost as 2 Snickers, how much is Julia's change if she gave the cashier 2 $10 bills?"""
    # Define the cost of a piece of Snickers and a pack of M&M's
    SNICKERS_COST = 1.5
    MM_COST = SNICKERS_COST * 2

    # Calculate the total cost of Julia's purchase
    total_cost = 2 * SNICKERS_COST + 3 * MM_COST

    # Calculate the total amount of money Julia gave to the cashier
    total_payment = 2 * 10

    # Calculate Julia's change
    change = total_payment - total_cost

    # return the result
    result = change
    return result

print(solution())