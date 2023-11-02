def solution():
    """Alexander is going food shopping. If he buys 5 apples for $1 each and 2 oranges for $2 each, how much does he spend?"""
    # Define the prices of apples and oranges
    apple_price = 1
    orange_price = 2

    # Define the number of apples and oranges purchased
    num_apples = 5
    num_oranges = 2

    # Calculate the total cost of the purchase
    total_cost = (apple_price * num_apples) + (orange_price * num_oranges)

    # Return the result
    result = total_cost
    return result

print(solution())