def solution():
    # Calculate the cost of one white sock
    one_white_sock_cost = 45 / 2

    # Calculate the cost of one brown sock
    one_brown_sock_cost = one_white_sock_cost - 0.25

    # Calculate the total cost of 15 brown socks
    total_brown_sock_cost = 15 * one_brown_sock_cost

    result = total_brown_sock_cost
    return result

print(solution())