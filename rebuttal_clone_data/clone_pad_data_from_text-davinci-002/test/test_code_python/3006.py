def solution():
    total_eggs = 3 * 12
    eggs_per_omelet = 4
    total_omelets = total_eggs / eggs_per_omelet
    omelets_per_person = total_omelets / 3
    result = omelets_per_person
    
    return result

print(solution())