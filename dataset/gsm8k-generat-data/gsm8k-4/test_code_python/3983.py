def solution():
    """Roberta wants to have a dinner party centered around soufflés. Each savory souffle calls for 8 eggs each and the dessert ones call for 6 eggs each. She wants to make 3 savory soufflés and 5 dessert soufflés for the party. How many eggs will she need?"""
    # Define the number of eggs needed for each type of souffle
    savory_eggs = 8
    dessert_eggs = 6

    # Define the number of souffles Roberta wants to make
    savory_souffles = 3
    dessert_souffles = 5

    # Calculate the total number of eggs needed
    total_eggs = (savory_eggs * savory_souffles) + (dessert_eggs * dessert_souffles)

    result = total_eggs
    return result

print(solution())