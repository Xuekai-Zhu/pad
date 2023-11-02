def solution():
    
    black_socks = 6
    white_socks = 4 * black_socks
    lost_white_socks = 0.5 * white_socks
    remaining_white_socks = white_socks - lost_white_socks
    difference = remaining_white_socks - black_socks
    result = difference
    return result

print(solution())