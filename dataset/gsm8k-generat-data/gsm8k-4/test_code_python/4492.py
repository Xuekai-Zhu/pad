def solution():
    """Jane bought 2 skirts for $13 each. She also bought 3 blouses for $6 each. She paid the cashier $100. How much change did she receive?"""
    # Calculate the total cost of the skirts
    skirts_cost = 2 * 13

    # Calculate the total cost of the blouses
    blouses_cost = 3 * 6

    # Calculate the total cost of the purchase
    total_cost = skirts_cost + blouses_cost

    # Calculate the change received by Jane
    change = 100 - total_cost

    # return the result
    result = change
    return result

print(solution())