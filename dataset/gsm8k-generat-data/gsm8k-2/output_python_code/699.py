def solution():
    """Two white socks cost 25 cents more than a single brown sock. If two white socks cost 45 cents, how much would you pay for 15 brown socks?"""
    white_sock_cost = 45 / 2
    brown_sock_cost = white_sock_cost - 0.25
    total_brown_sock_cost = 15 * brown_sock_cost
    result = total_brown_sock_cost
    return result

print(solution())