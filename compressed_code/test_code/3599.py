def solution():
    
    colored_pencils = 14
    black_pencils = 35
    total_pencils = colored_pencils + black_pencils
    remaining_pencils = total_pencils - 10
    siblings = 3
    pencils_per_sibling = remaining_pencils // siblings
    result = pencils_per_sibling
    return result

print(solution())