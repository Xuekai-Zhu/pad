def solution():
    
    total_shells = 700
    alphas_shells = total_shells * 0.4
    remaining_shells = total_shells - alphas_shells
    finders_shells = remaining_shells * 0.6
    gogetters_shells = remaining_shells - finders_shells
    result = gogetters_shells
    return result

print(solution())