def solution():
    num_savory = 3
    num_dessert = 5
    eggs_per_savory = 8
    eggs_per_dessert = 6

    # Calculate the total number of eggs needed for savory souffles
    total_savory_eggs = num_savory * eggs_per_savory

    # Calculate the total number of eggs needed for dessert souffles
    total_dessert_eggs = num_dessert * eggs_per_dessert

    # Calculate the total number of eggs needed for the party
    total_eggs_needed = total_savory_eggs + total_dessert_eggs
    result = total_eggs_needed
    return result

print(solution())