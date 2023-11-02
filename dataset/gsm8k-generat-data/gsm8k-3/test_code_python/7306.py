def solution():
    """Roxanne bought 2 cups of lemonade for $2 each and 2 sandwiches for $2.50 each. How much change must she get from a $20 bill?"""
    # Define the prices of the items
    LEMONADE_PRICE = 2
    SANDWICH_PRICE = 2.5

    # Calculate the total cost of the items
    total_cost = 2 * LEMONADE_PRICE + 2 * SANDWICH_PRICE

    # Calculate the amount of change needed from a $20 bill
    change = 20 - total_cost

    # Display the amount of change needed
    result = change
    return result

print(solution())