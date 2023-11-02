def solution():
    total_parents = 120
    excellent = 0.15 * total_parents
    very_satisfactory = 0.6 * total_parents
    remaining_parents = total_parents - excellent - very_satisfactory
    satisfactory = 0.8 * remaining_parents
    needs_improvement = remaining_parents - satisfactory
    result = needs_improvement
    return result

print(solution())