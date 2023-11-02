def solution():
    kevin_eggs = 5
    bonnie_eggs = 13
    george_eggs = 9
    cheryl_eggs = 56
    total_other_eggs = kevin_eggs + bonnie_eggs + george_eggs
    cheryls_eggs_more = cheryl_eggs - total_other_eggs
    result = cheryls_eggs_more
    return result

print(solution())