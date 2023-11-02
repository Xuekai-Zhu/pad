def solution():
    # Calculate the number of black socks
    black_socks = 20 / 2

    # Calculate the total number of red and black socks
    red_black_total = 20 + black_socks

    # Calculate the number of white socks
    white_socks = 2 * (red_black_total)

    # Calculate the total number of socks
    total_socks = red_black_total + white_socks
    result = total_socks
    return result

print(solution())