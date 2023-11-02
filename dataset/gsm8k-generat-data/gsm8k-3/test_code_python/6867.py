def solution():
    """Jack is a soccer player. He needs to buy two pairs of socks and a pair of soccer shoes. Each pair of socks cost $9.50, and the shoes cost $92. Jack has $40. How much more money does Jack need?"""
    # Define the cost of each item
    SOCKS_COST = 9.5
    SHOES_COST = 92

    # Define the number of each item needed
    socks_needed = 2
    shoes_needed = 1

    # Calculate the total cost of the socks
    socks_cost = SOCKS_COST * socks_needed

    # Calculate the total cost of the shoes
    shoes_cost = SHOES_COST * shoes_needed

    # Calculate the total cost of all the items
    total_cost = socks_cost + shoes_cost

    # Calculate how much more money Jack needs
    remaining_money = total_cost - 40

    # Display how much more money Jack needs
    result = remaining_money
    return result

print(solution())