def solution():
    red_socks = 20
    black_socks = red_socks / 2
    white_socks = (red_socks + black_socks) * 2

    # Calculate the total number of socks
    total_socks = red_socks + black_socks + white_socks
    result = total_socks
    return result

print(solution())