def solution():
    """John Smith buys 3 cakes for $12 each and splits the cost with his brother. How much did he pay?"""
    # Define the number of cakes and the cost per cake
    num_cakes = 3
    cost_per_cake = 12

    # Calculate the total cost of the cakes
    total_cost = num_cakes * cost_per_cake

    # Calculate John Smith's half of the total cost
    john_cost = total_cost / 2

    result = john_cost
    return result

print(solution())