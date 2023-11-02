def solution():
    """Pauly is making omelets for his family. There are three dozen eggs, and he plans to use them all. Each omelet requires 4 eggs. Including himself, there are 3 people. How many omelets does each person get?"""
    num_eggs = 3 * 12
    num_people = 3
    eggs_per_omelet = 4
    total_omelets = num_eggs // eggs_per_omelet
    omelets_per_person = total_omelets // num_people
    result = omelets_per_person
    return result

print(solution())