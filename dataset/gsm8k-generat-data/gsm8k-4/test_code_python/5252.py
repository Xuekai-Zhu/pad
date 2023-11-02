def solution():
    """A survey was conducted by a school to the parents about their children's online class experience. Fifteen percent of the respondents rated Excellent; 60% rated Very Satisfactory; 80% of the remaining respondents rated Satisfactory and the rest rated Needs Improvement. If 120 parents answered the survey, how many of them rated Needs Improvement?"""
    # Define the total number of parents who answered the survey
    total_parents = 120

    # Calculate the number of parents who rated Excellent
    excellent_parents = total_parents * 0.15

    # Calculate the number of parents who rated Very Satisfactory
    very_satisfactory_parents = total_parents * 0.6

    # Calculate the number of remaining parents
    remaining_parents = total_parents - excellent_parents - very_satisfactory_parents

    # Calculate the number of parents who rated Satisfactory
    satisfactory_parents = remaining_parents * 0.8

    # Calculate the number of parents who rated Needs Improvement
    needs_improvement_parents = total_parents - excellent_parents - very_satisfactory_parents - satisfactory_parents

    # Return the result
    result = needs_improvement_parents
    return result

print(solution())