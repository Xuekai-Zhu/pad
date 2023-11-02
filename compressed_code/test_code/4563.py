def solution():
    
    total_bollards = 4000 * 2
    installed_bollards = total_bollards * 3 / 4
    remaining_bollards = total_bollards - installed_bollards
    result = remaining_bollards
    return result

print(solution())