def solution():
    num_adults = 3
    num_eggs_per_dozen = 12
    num_eggs = 3 * num_adults  # Each adult gets 3 eggs
    num_girls = 7
    num_boys = 0

    # Calculate the total number of eggs for the girls
    num_girls_eggs = num_girls

    # Calculate the total number of eggs for the boys
    total_eggs_for_children = num_eggs - num_girls_eggs
    num_boys_eggs = (total_eggs_for_children - num_boys) / (num_boys + num_girls)

    # Calculate the total number of boys
    num_boys = num_boys_eggs - num_girls

    result = num_boys
    return result

print(solution())