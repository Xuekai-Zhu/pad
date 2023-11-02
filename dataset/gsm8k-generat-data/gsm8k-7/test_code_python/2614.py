def solution():
    eggs_per_dozen = 12
    initial_eggs = 2 * eggs_per_dozen
    neighbor_eggs = 1 * eggs_per_dozen
    omelet_eggs = 2
    cake_eggs = 4

    # Calculate the total number of eggs Megan has left
    remaining_eggs = initial_eggs + neighbor_eggs - omelet_eggs - cake_eggs

    # Calculate the number of eggs per meal Megan can have
    eggs_per_meal = remaining_eggs / 3

    result = eggs_per_meal
    return result

print(solution())