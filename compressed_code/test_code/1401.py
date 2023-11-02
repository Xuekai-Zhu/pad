def solution():
    
    total_eggs = 6 * 12
    used_eggs = total_eggs / 2
    remaining_eggs = total_eggs - used_eggs
    remaining_eggs -= 15
    result = remaining_eggs
    return result

print(solution())