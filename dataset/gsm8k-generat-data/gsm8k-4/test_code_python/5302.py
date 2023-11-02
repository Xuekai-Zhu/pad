def solution():
    """Pauly is making omelets for his family. There are three dozen eggs, and he plans to use them all. Each omelet requires 4 eggs. Including himself, there are 3 people. How many omelets does each person get?"""
    # Define the total number of eggs
    total_eggs = 3 * 12

    # Calculate the total number of omelets that can be made
    total_omelets = total_eggs // 4

    # Calculate the number of omelets each person gets
    omelets_per_person = total_omelets // 3

    # return the result
    result = omelets_per_person
    return result

print(solution())