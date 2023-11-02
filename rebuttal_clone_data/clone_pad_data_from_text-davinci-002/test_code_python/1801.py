def solution():
    total_eggs = 6 * 12
    used_eggs = total_eggs / 2
    broken_eggs = 15
    eggs_left = total_eggs - used_eggs - broken_eggs
    result = eggs_left
    
    return result

print(solution())