def solution():
    # Calculate the cost of a single white sock
    cost_white_sock = 45 / 2  # Two white socks cost 45 cents
    # Two white socks cost 25 cents more than a single brown sock
    # Therefore, the cost of a single brown sock is:
    cost_brown_sock = cost_white_sock - 0.25

    # Calculate the total cost of 15 brown socks
    total_cost_brown_socks = cost_brown_sock * 15
    result = total_cost_brown_socks
    return result

print(solution())