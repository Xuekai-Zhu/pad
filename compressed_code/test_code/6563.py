def solution():
    
    pool_capacity = 60
    fill_rate = 1.6
    leak_rate = 0.1
    net_fill_rate = fill_rate - leak_rate
    time_to_fill = pool_capacity / net_fill_rate
    result = time_to_fill
    return result

print(solution())