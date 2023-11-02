def solution():
    # Calculate the total number of eggs Megan had
    total_eggs = 2*12 + 4 + 12

    # Calculate how many eggs Megan had left after making the omelet and cake
    remaining_eggs = total_eggs - 6

    # Calculate how many eggs Megan gave to her aunt
    aunt_eggs = remaining_eggs / 2

    # Calculate how many eggs Megan has left
    remaining_eggs = remaining_eggs - aunt_eggs

    # Calculate how many eggs Megan has for each of her next 3 meals
    eggs_per_meal = remaining_eggs / 3
    result = eggs_per_meal
    return result

print(solution())