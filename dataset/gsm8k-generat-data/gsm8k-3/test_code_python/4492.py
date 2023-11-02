def solution():
    """Jane bought 2 skirts for $13 each. She also bought 3 blouses for $6 each. She paid the cashier $100. How much change did she receive?"""
    # Calculate the cost of the skirts
    skirt_cost = 2 * 13

    # Calculate the cost of the blouses
    blouse_cost = 3 * 6

    # Calculate the total cost
    total_cost = skirt_cost + blouse_cost

    # Calculate the change
    change = 100 - total_cost

    # Display the change
    result = change
    return result

print(solution())