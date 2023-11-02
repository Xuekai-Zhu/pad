def solution():
    
    initial_eggs = 24
    used_eggs = 2 + 4
    remaining_eggs = initial_eggs - used_eggs
    aunt_eggs = remaining_eggs / 2
    remaining_eggs -= aunt_eggs
    eggs_per_meal = remaining_eggs / 3
    result = eggs_per_meal
    return result

print(solution())