def solution():
    """Luis needed to buy some socks. He bought 4 pairs of red socks and 6 pairs of blue ones. In total, he spent $42. If the red socks cost $3 each, how much did he pay for each blue pair?"""
    # Define the number of red and blue socks
    red_socks = 4 * 2  # 4 pairs of red socks that have 2 socks per pair
    blue_socks = 6 * 2  # 6 pairs of blue socks that have 2 socks per pair

    # Define the total cost of socks
    total_cost = 42

    # Calculate the cost of the red socks
    red_cost = red_socks * 3

    # Calculate the cost of the blue socks
    blue_cost = total_cost - red_cost

    # Calculate the cost per pair of blue socks
    blue_pair_cost = blue_cost / 6

    result = blue_pair_cost
    return result

print(solution())