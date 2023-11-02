def solution():
    # Calculate the total cost of the red socks
    red_socks_cost = 4 * 3  # 4 pairs of red socks at $3 per pair

    # Calculate the cost of the blue socks
    total_cost = 42  # total spent by Luis
    blue_socks_cost = total_cost - red_socks_cost  # cost of blue socks

    # Calculate the cost per blue pair
    blue_pairs = 6
    cost_per_blue_pair = blue_socks_cost / blue_pairs

    result = cost_per_blue_pair
    return result

print(solution())