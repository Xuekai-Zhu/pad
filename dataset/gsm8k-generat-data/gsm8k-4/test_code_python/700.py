def solution():
    """Two white socks cost 25 cents more than a single brown sock. If two white socks cost 45 cents, how much would you pay for 15 brown socks?"""
    # Define the cost of one brown sock
    brown_sock_cost = None

    # Calculate the cost of two brown socks
    two_brown_socks_cost = 2 * brown_sock_cost

    # Calculate the cost of two white socks
    two_white_socks_cost = 45

    # Calculate the difference in cost between two white socks and two brown socks
    cost_difference = two_white_socks_cost - two_brown_socks_cost

    # Calculate the cost of one white sock
    white_sock_cost = cost_difference / 2

    # Calculate the cost of 15 brown socks
    fifteen_brown_socks_cost = 15 * brown_sock_cost

    # Calculate the cost of 30 white socks
    thirty_white_socks_cost = 30 * white_sock_cost

    # Calculate the total cost of all the socks
    total_cost = fifteen_brown_socks_cost + thirty_white_socks_cost

    result = total_cost
    return result

print(solution())