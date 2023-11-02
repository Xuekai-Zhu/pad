def solution():
    savory_souffle_eggs = 8  # Each savory souffle uses 8 eggs
    dessert_souffle_eggs = 6  # Each dessert souffle uses 6 eggs
    num_savory_souffles = 3  # Roberta wants to make 3 savory souffles
    num_dessert_souffles = 5  # Roberta wants to make 5 dessert souffles

    # Calculate the total number of eggs needed
    total_eggs = (savory_souffle_eggs * num_savory_souffles) + (dessert_souffle_eggs * num_dessert_souffles)
    result = total_eggs
    return result

print(solution())