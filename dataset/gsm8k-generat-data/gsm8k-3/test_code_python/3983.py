def solution():
    """Roberta wants to have a dinner party centered around soufflés.  Each savory souffle calls for 8 eggs each and the dessert ones call for 6 eggs each.  She wants to make 3 savory soufflés and 5 dessert soufflés for the party.  How many eggs will she need?"""
    # Define the number of eggs needed for each type of soufflé
    SAVORY_SOUFFLE_EGGS = 8
    DESSERT_SOUFFLE_EGGS = 6

    # Define the number of each type of soufflé to be made
    savory_souffle_count = 3
    dessert_souffle_count = 5

    # Calculate the total number of eggs needed
    total_eggs = (SAVORY_SOUFFLE_EGGS * savory_souffle_count) + (DESSERT_SOUFFLE_EGGS * dessert_souffle_count)

    # Display the total number of eggs needed
    result = total_eggs
    return result

print(solution())