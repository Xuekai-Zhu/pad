def solution():
    
    initial_cj = 80
    initial_snatch = 50
    new_cj = initial_cj * 2
    snatch_increase = initial_snatch * 0.8
    new_snatch = initial_snatch + snatch_increase
    total_capacity = new_cj + new_snatch
    result = total_capacity
    return result

print(solution())