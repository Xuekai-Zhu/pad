def solution():
    
    initial_collapse = 4
    total_collapse = initial_collapse + (2**1 * initial_collapse) + (2**2 * initial_collapse) + (2**3 * initial_collapse)
    result = total_collapse
    return result

print(solution())