def solution():
    """Alexander is going food shopping. If he buys 5 apples for $1 each and 2 oranges for $2 each, how much does he spend?"""
    # Define the cost of each item
    APPLE_PRICE = 1
    ORANGE_PRICE = 2

    # Define the number of each item purchased
    num_apples = 5
    num_oranges = 2

    # Calculate the total cost
    total_cost = (num_apples * APPLE_PRICE) + (num_oranges * ORANGE_PRICE)

    # Display the total cost
    result = total_cost
    return result

print(solution())