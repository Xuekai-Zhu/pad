def solution():
    """A survey was conducted by a school to the parents about their children's online class experience. Fifteen percent of the respondents rated Excellent; 60% rated Very Satisfactory; 80% of the remaining respondents rated Satisfactory and the rest rated Needs Improvement. If 120 parents answered the survey, how many of them rated Needs Improvement?"""
    total_parents = 120
    excellent_percent = 0.15
    very_satisfactory_percent = 0.6
    satisfactory_percent = 0.8
    excellent_count = total_parents * excellent_percent
    very_satisfactory_count = total_parents * very_satisfactory_percent
    remaining_parents_count = total_parents - excellent_count - very_satisfactory_count
    satisfactory_count = remaining_parents_count * satisfactory_percent
    needs_improvement_count = total_parents - excellent_count - very_satisfactory_count - satisfactory_count
    result = needs_improvement_count
    return result

print(solution())