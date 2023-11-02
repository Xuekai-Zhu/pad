def solution():
    # Calculate the total number of eggs Megan has
    total_eggs = 12 + 12  # bought one dozen eggs and received another from the neighbor
    total_eggs -= 2  # used 2 eggs to make an omelet
    total_eggs -= 4  # used 4 eggs to bake a cake
    remaining_eggs = total_eggs / 2  # gave half of the remaining eggs to her aunt
    eggs_per_meal = remaining_eggs / 3  # plans to divide what's left equally for her next 3 meals
    result = eggs_per_meal
    return result

print(solution())