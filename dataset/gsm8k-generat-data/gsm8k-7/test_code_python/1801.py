def solution():
    eggs_per_dozen = 12
    total_eggs = 6 * eggs_per_dozen    # total number of eggs purchased
    used_eggs = 0.5 * total_eggs       # number of eggs used in two weeks
    remaining_eggs = total_eggs - used_eggs - 15   # number of eggs remaining after accidentally breaking 15
    result = remaining_eggs
    return result

print(solution())