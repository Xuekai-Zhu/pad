def solution():
    total_socks = 180
    white_sock_ratio = 2 / 3
    blue_sock_ratio = 1 - white_sock_ratio

    # Calculate the number of white socks
    num_white_socks = total_socks * white_sock_ratio

    # Calculate the number of blue socks
    num_blue_socks = total_socks * blue_sock_ratio
    result = num_blue_socks
    return result

print(solution())