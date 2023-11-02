def solution():
    white_socks = 4
    black_socks = 1
    lost_socks = white_socks / 2
    remaining_white_socks = white_socks - lost_socks
    remaining_socks_difference = remaining_white_socks - black_socks
    result = remaining_socks_difference
    return result

print(solution())