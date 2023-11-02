def solution():
    """A survey was conducted by a school to the parents about their children's online class experience. Fifteen percent of the respondents rated Excellent; 60% rated Very Satisfactory; 80% of the remaining respondents rated Satisfactory and the rest rated Needs Improvement. If 120 parents answered the survey, how many of them rated Needs Improvement?"""
    # Calculate the number of respondents who rated Excellent
    excellent = 0.15 * 120

    # Calculate the number of respondents who rated Very Satisfactory
    very_satisfactory = 0.6 * 120

    # Calculate the number of remaining respondents
    remaining = 120 - excellent - very_satisfactory

    # Calculate the number of respondents who rated Satisfactory
    satisfactory = 0.8 * remaining

    # Calculate the number of respondents who rated Needs Improvement
    needs_improvement = remaining - satisfactory

    # Display the number of respondents who rated Needs Improvement
    result = needs_improvement
    return result

print(solution())