def solution():
    """John Smith buys 3 cakes for $12 each and splits the cost with his brother.  How much did he pay?"""
    # Define the number of cakes and the price per cake
    num_cakes = 3
    cake_price = 12

    # Calculate the total cost
    total_cost = num_cakes * cake_price

    # Split the cost with John's brother
    john_cost = total_cost / 2

    # Display John's cost
    result = john_cost
    return result

print(solution())