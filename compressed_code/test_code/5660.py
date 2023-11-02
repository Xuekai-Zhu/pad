def solution():
    
    total_pickles = min(4*12, 10*6)
    jars_needed = (total_pickles+11) // 12
    vinegar_needed = jars_needed * 10
    vinegar_left = max(0, 100 - vinegar_needed)
    result = vinegar_left
    return result

print(solution())