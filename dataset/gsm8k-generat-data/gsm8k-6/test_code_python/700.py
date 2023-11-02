def solution():
    # Find the cost of one white sock
    one_white_sock = 45 / 2  # two white socks cost 45 cents
    # Find the cost of one brown sock
    one_brown_sock = one_white_sock - 0.25  # two white socks cost 25 cents more than a single brown sock
    # Find the cost of 15 brown socks
    total_cost_of_brown_socks = one_brown_sock * 15
    result = total_cost_of_brown_socks
    return result

print(solution())