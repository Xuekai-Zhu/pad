def solution():
    
    total_size = 2300
    living_size = 1000
    guest_size = (1/5) * (total_size - living_size)
    master_size = total_size - living_size - guest_size
    result = master_size
    return result

print(solution())