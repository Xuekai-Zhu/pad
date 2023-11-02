def solution():
    """Bill picked 50 apples from the orchard with his wife and two children. He sends each of his kids to school with 3 apples for their two favorite teachers. His wife Jill bakes two apple pies, using 10 apples per pie. How many apples does Bill have left?"""
    # Define the initial number of apples
    initial_apples = 50

    # Calculate the number of apples given to the kids' teachers
    apples_given_to_teachers = 2 * 2 * 3

    # Calculate the number of apples used for the pies
    apples_used_for_pies = 2 * 10

    # Calculate the number of apples left
    apples_left = initial_apples - apples_given_to_teachers - apples_used_for_pies
    result = apples_left
    return result

print(solution())