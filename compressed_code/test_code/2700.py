def solution():
    
    total_eggs = 3 * 12
    crepe_eggs = total_eggs // 4
    remaining_eggs = total_eggs - crepe_eggs
    cupcake_eggs = (2/3) * remaining_eggs
    sunny_eggs = remaining_eggs - cupcake_eggs
    result = sunny_eggs
    return result

print(solution())