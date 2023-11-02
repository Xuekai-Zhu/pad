def solution():
    initial_num_socks = 12
    sandras_socks = 20
    cousins_socks = sandras_socks / 5
    moms_socks = initial_num_socks * 3 + 8
    total_socks = initial_num_socks + sandras_socks + cousins_socks + moms_socks
    result = total_socks
    
    return result

print(solution())