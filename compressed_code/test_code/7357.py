def solution():
    
    flow_rate = 24
    basin_capacity = 260
    leak_rate = 4
    effective_flow_rate = flow_rate - leak_rate
    time_to_fill = basin_capacity / effective_flow_rate
    result = time_to_fill
    return result

print(solution())