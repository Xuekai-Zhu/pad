def solution():
    num_red_socks = 4
    red_sock_price = 3

    num_blue_socks = 6
    total_cost = 42

    # Calculate the total cost of all red socks
    total_red_socks_cost = num_red_socks * red_sock_price

    # Calculate the cost of all blue socks
    total_blue_socks_cost = total_cost - total_red_socks_cost

    # Calculate the cost per pair of blue socks
    blue_sock_price = total_blue_socks_cost / num_blue_socks
    result = blue_sock_price
    return result

print(solution())