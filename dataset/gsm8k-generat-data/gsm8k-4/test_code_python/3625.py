def solution():
    """At Ken's local store, a pound of steak is going for $7. He decides to get two pounds. At the till, he pays using a $20 bill. How much money will he get back?"""
    # Define the cost of one pound of steak and the number of pounds Ken bought
    COST_PER_POUND = 7
    POUNDS_BOUGHT = 2

    # Calculate the total cost of the steak
    total_cost = COST_PER_POUND * POUNDS_BOUGHT

    # Calculate the amount Ken will receive in change
    change = 20 - total_cost

    # Return the result
    result = change
    return result

print(solution())