def solution():
    
    barrel_size = 7
    num_barrels = 4
    total_volume = barrel_size * num_barrels
    flow_rate = 3.5
    time = total_volume / flow_rate
    result = time
    return result

print(solution())