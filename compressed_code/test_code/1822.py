def solution():
    
    egg_weight = 1/16
    total_weight = 6
    total_eggs = int(total_weight / egg_weight)
    dozen_eggs = total_eggs / 12
    result = dozen_eggs
    return result

print(solution())