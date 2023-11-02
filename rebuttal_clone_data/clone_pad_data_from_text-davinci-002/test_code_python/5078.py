def solution():
    dozen_eggs = 24
    dropped_eggs = 3 + (2 * 2)
    cracked_eggs = dropped_eggs
    perfect_eggs = dozen_eggs - cracked_eggs
    result = perfect_eggs - cracked_eggs
    return result

print(solution())