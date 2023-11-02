def solution():
    total_chickens = 80
    neighbor_chickens = 12
    gate_chickens = 25

    chickens_left = total_chickens - neighbor_chickens - gate_chickens
    result = chickens_left
    return result

print(solution())