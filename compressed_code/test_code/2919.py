def solution():
    
    num_fleas_after = 14
    num_fleas_before = num_fleas_after
    for i in range(4):
        num_fleas_before *= 2
    result = num_fleas_before - num_fleas_after
    return result

print(solution())