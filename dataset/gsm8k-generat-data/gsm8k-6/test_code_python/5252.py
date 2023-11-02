def solution():
    # Calculate the number of respondents who rated Excellent
    excellent = 0.15 * 120

    # Calculate the number of respondents who rated Very Satisfactory
    v_satisfactory = 0.6 * 120

    # Calculate the number of remaining respondents who rated Satisfactory
    remaining = 120 - excellent - v_satisfactory
    satisfactory = 0.8 * remaining

    # Calculate the number of respondents who rated Needs Improvement
    needs_improvement = 120 - excellent - v_satisfactory - satisfactory

    result = needs_improvement
    return result

print(solution())