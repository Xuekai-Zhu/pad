def solution():
    
    total_eggs = 2 * 12
    broken_eggs = 3
    cracked_eggs = 2 * 3
    perfect_eggs = total_eggs - broken_eggs - cracked_eggs
    difference = perfect_eggs - cracked_eggs
    result = difference
    return result

print(solution())