def solution():
    
    waterfall_rate = 24
    basin_capacity = 260
    leak_rate = 4
    net_rate = waterfall_rate - leak_rate
    time_to_fill = basin_capacity/net_rate
    result = time_to_fill
    return result

print(solution())