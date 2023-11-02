def solution():
    """Andy has 4 times as many white socks as he has black socks. If he loses half his white socks, how many more white socks does he still have than black socks if he has 6 black socks?"""
    black_socks = 6
    white_socks = 4 * black_socks
    lost_white_socks = 0.5 * white_socks
    remaining_white_socks = white_socks - lost_white_socks
    difference = remaining_white_socks - black_socks
    result = difference
    return result

print(solution())