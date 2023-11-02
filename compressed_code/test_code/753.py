def solution():
    
    pool_size = 60
    fill_rate = 1.6
    leak_rate = 0.1
    net_fill_rate = fill_rate - leak_rate
    fill_time = pool_size / net_fill_rate
    result = fill_time
    return result

print(solution())