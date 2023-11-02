def solution():
     white_socks_cost = 0.45
     white_sock_increase = 0.25
     brown_sock_cost = white_socks_cost - white_sock_increase
     total_cost = brown_sock_cost * 15
     result = total_cost
     return result

print(solution())