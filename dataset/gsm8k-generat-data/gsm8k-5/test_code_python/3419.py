def solution():
    num_red_pairs = 4  # Luis bought 4 pairs of red socks
    num_blue_pairs = 6  # Luis bought 6 pairs of blue socks
    total_cost = 42  # Luis spent $42 in total
    cost_per_red_pair = 3  # Red socks cost $3 per pair

    # Calculate the total cost of the blue socks
    total_cost_blue = total_cost - (num_red_pairs * cost_per_red_pair * 2) # Luis bought 4 pairs of red socks, so 2 socks per pair
    cost_per_blue_pair = total_cost_blue / num_blue_pairs
    result = cost_per_blue_pair
    return result

print(solution())