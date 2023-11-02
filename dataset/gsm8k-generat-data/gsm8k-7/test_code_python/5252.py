def solution():
    total_respondents = 120
    excellent = 0.15 * total_respondents
    very_satisfactory = 0.6 * total_respondents
    remaining_respondents = total_respondents - excellent - very_satisfactory
    satisfactory = 0.8 * remaining_respondents
    needs_improvement = remaining_respondents - satisfactory
    result = needs_improvement
    return result

print(solution())