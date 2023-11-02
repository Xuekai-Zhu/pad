def solution():
    red_socks = 20 * 2  # James has 20 pairs of red socks, which is 40 individual socks
    black_socks = red_socks / 2  # James has half as many black socks as red socks
    combined_red_black = red_socks + black_socks  # Combined number of red and black socks
    white_socks = combined_red_black * 2  # James has twice as many white socks as red and black combined

    # Calculate the total number of socks
    total_socks = red_socks + black_socks + white_socks
    result = total_socks
    return result

print(solution())