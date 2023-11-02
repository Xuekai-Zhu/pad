def solution():
    """Luis needed to buy some socks. He bought 4 pairs of red socks and 6 pairs of blue ones. In total, he spent $42. If the red socks cost $3 each, how much did he pay for each blue pair?"""
    red_socks = 4
    blue_socks = 6
    red_cost = 3
    total_cost = 42
    total_red_cost = red_socks * red_cost
    blue_cost = (total_cost - total_red_cost) / blue_socks / 2
    result = blue_cost
    return result

print(solution())