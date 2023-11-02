def solution():
    
    tractor_rate = 75
    darrel_rate = 10
    total_rate = tractor_rate + darrel_rate
    compost_needed = 2550
    time_to_load = compost_needed / total_rate
    result = time_to_load
    return result

print(solution())