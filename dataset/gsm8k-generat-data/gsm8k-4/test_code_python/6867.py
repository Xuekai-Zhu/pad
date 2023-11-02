def solution():
    """Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?"""
    # Define the cost of each item
    sock_cost = 9.5
    shoe_cost = 92

    # Calculate the total cost of the socks
    total_sock_cost = sock_cost * 2

    # Calculate the total cost of the purchase
    total_cost = total_sock_cost + shoe_cost

    # Calculate how much more money Jack needs
    remaining_money = total_cost - 40

    # Return the result
    result = remaining_money
    return result

print(solution())