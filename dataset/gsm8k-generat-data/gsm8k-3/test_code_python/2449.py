def solution():
    """Yanna bought ten shirts at $5 each and three pairs of sandals at $3 each.  How much change did she get back if she gave a one hundred dollar bill?"""
    # Define the cost of each item
    SHIRT_PRICE = 5
    SANDALS_PRICE = 3

    # Define the number of each item purchased
    shirt_count = 10
    sandals_count = 3

    # Calculate the total cost of the shirts
    shirt_cost = shirt_count * SHIRT_PRICE

    # Calculate the total cost of the sandals
    sandals_cost = sandals_count * SANDALS_PRICE

    # Calculate the total cost of all items
    total_cost = shirt_cost + sandals_cost

    # Calculate the change Yanna will receive
    change = 100 - total_cost

    # Display the change
    result = round(change,2)
    return result

print(solution())