def solution():
    num_red_socks = 6
    num_blue_socks = 2 * num_red_socks
    num_black_socks = num_blue_socks - 3
    num_white_socks = num_red_socks + 1

    # Calculate the total number of socks
    total_socks = num_red_socks + num_blue_socks + num_black_socks + num_white_socks

    # Calculate the total number of pairs of socks
    total_pairs = total_socks // 2

    result = total_socks
    return result

print(solution())