def solution():
    
    total_chickens = 80
    neighbor_chickens = 12
    gate_chickens = 25
    remaining_chickens = total_chickens - neighbor_chickens - gate_chickens
    result = remaining_chickens
    return result

print(solution())