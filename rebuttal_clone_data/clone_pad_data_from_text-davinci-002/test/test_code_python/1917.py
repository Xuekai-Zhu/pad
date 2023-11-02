def solution():
    total_socks = 10
    total_cost = 42
    red_socks = 4
    red_sock_cost = 3
    blue_sock_cost = (total_cost - (red_socks * red_sock_cost)) / 6
    result = blue_sock_cost
    return result

print(solution())