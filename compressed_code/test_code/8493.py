def solution():
    
    total_socks = 10
    total_cost = 42
    red_socks = 4
    red_sock_cost = 3
    total_red_cost = red_socks * red_sock_cost
    blue_cost = (total_cost - total_red_cost) / (total_socks - red_socks)
    result = blue_cost
    return result

print(solution())