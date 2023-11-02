def solution():
    """Pauly is making omelets for his family. There are three dozen eggs, and he plans to use them all. Each omelet requires 4 eggs. Including himself, there are 3 people. How many omelets does each person get?"""
    # Define the total number of eggs
    eggs = 3 * 12

    # Calculate the total number of omelets
    omelets = eggs // 4

    # Calculate the number of omelets per person
    omelets_per_person = omelets // 3

    # Display the number of omelets per person
    result = omelets_per_person
    return result

print(solution())