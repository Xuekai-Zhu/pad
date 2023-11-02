def solution():
    """Bill picked 50 apples from the orchard with his wife and two children.  He sends each of his kids to school with 3 apples for their two favorite teachers.  His wife Jill bakes two apple pies, using 10 apples per pie. How many apples does Bill have left?"""
    # Starting with 50 apples
    apples = 50

    # Subtracting the amount given to the kids' teachers
    apples -= 2 * 2 * 3

    # Subtracting the amount used for the apple pies
    apples -= 2 * 10

    # Displaying the remaining amount of apples
    result = apples
    return result

print(solution())