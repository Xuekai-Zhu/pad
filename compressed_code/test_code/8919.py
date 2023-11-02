def solution():
    
    base_recess = 20
    extra_A = 2
    extra_B = 1
    reduced_D = -1
    A_count = 10
    B_count = 12
    C_count = 14
    D_count = 5
    total_recess = base_recess + (extra_A * A_count) + (extra_B * B_count) + (reduced_D * D_count)
    result = total_recess
    return result

print(solution())