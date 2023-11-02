def solution():
    """Bill picked 50 apples from the orchard with his wife and two children. He sends each of his kids to school with 3 apples for their two favorite teachers. His wife Jill bakes two apple pies, using 10 apples per pie. How many apples does Bill have left?"""
    total_apples = 50
    apples_for_teachers = 2 * 2 * 3
    apples_for_pies = 2 * 10
    remaining_apples = total_apples - apples_for_teachers - apples_for_pies
    result = remaining_apples
    return result

print(solution())