def solution():
    """At Ken's local store, a pound of steak is going for $7. He decides to get two pounds. At the till, he pays using a $20 bill. How much money will he get back?"""
    # Define the cost per pound of steak and the number of pounds purchased
    COST_PER_POUND = 7
    POUNDS_PURCHASED = 2

    # Calculate the total cost of the steaks
    total_cost = COST_PER_POUND * POUNDS_PURCHASED

    # Calculate the amount of change Ken will receive
    change = 20 - total_cost

    # Display the amount of change
    result = change
    return result

print(solution())