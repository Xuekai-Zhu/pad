def solution():
    """Two white socks cost 25 cents more than a single brown sock. If two white socks cost 45 cents, how much would you pay for 15 brown socks?"""
    cost_of_two_white_socks = 45
    cost_of_single_brown_sock = (cost_of_two_white_socks - 25) / 2
    cost_of_fifteen_brown_socks = 15 * cost_of_single_brown_sock
    result = cost_of_fifteen_brown_socks
    return result

print(solution())