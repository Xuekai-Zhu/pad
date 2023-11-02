def solution():
    cost_of_two_white_socks = 45
    extra_cost_of_two_white_socks = 25

    # Calculate the cost of one white sock
    cost_of_one_white_sock = (cost_of_two_white_socks - extra_cost_of_two_white_socks) / 2

    # Calculate the cost of one brown sock
    cost_of_one_brown_sock = cost_of_one_white_sock - extra_cost_of_two_white_socks

    # Calculate the cost of 15 brown socks
    total_cost_of_brown_socks = 15 * cost_of_one_brown_sock
    result = total_cost_of_brown_socks
    return result

print(solution())