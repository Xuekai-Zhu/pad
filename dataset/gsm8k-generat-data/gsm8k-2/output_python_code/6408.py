def solution():
    """James has 20 pairs of red socks and half as many black socks. He has twice as many white socks as red and black combined. How many total socks does he have combined?"""
    red_socks = 20 * 2  # 20 pairs of socks is equivalent to 40 individual socks
    black_socks = red_socks / 2
    combined_rb_socks = red_socks + black_socks
    white_socks = combined_rb_socks * 2
    total_socks = red_socks + black_socks + white_socks
    result = total_socks
    return result

print(solution())