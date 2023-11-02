def solution():
    """Roberta wants to have a dinner party centered around soufflés. Each savory souffle calls for 8 eggs each and the dessert ones call for 6 eggs each. She wants to make 3 savory soufflés and 5 dessert soufflés for the party. How many eggs will she need?"""
    savory_souffle_eggs = 8
    dessert_souffle_eggs = 6
    num_savory_souffles = 3
    num_dessert_souffles = 5
    total_eggs = (savory_souffle_eggs * num_savory_souffles) + (dessert_souffle_eggs * num_dessert_souffles)
    result = total_eggs
    return result

print(solution())