def solution():
    penny_initial = 20
    sock_cost = 2
    num_socks = 4
    hat_cost = 7
    penny_final = penny_initial - (sock_cost * num_socks) - hat_cost
    result = penny_final
    return result

print(solution())