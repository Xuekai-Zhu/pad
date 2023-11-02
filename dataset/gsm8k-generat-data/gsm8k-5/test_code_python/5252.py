def solution():
    # Total number of parents who answered the survey
    total_parents = 120

    # Number of parents who rated Excellent
    excellent = 0.15 * total_parents

    # Number of parents who rated Very Satisfactory
    very_satisfactory = 0.6 * total_parents

    # Number of remaining parents
    remaining_parents = total_parents - excellent - very_satisfactory

    # Number of parents who rated Satisfactory
    satisfactory = 0.8 * remaining_parents

    # Number of parents who rated Needs Improvement
    needs_improvement = remaining_parents - satisfactory

    result = needs_improvement
    return result

print(solution())