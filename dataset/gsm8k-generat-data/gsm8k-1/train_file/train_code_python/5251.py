def solution():
    """A survey was conducted by a school to the parents about their children's online class experience. Fifteen percent of the respondents rated Excellent; 60% rated Very Satisfactory; 80% of the remaining respondents rated Satisfactory and the rest rated Needs Improvement. If 120 parents answered the survey, how many of them rated Needs Improvement?"""
    total_respondents = 120
    
    excellent_rating_percent = 15
    excellent_rating_count = (excellent_rating_percent / 100) * total_respondents
    
    very_satisfactory_rating_percent = 60
    very_satisfactory_rating_count = (very_satisfactory_rating_percent / 100) * total_respondents
    
    remaining_respondents = total_respondents - excellent_rating_count - very_satisfactory_rating_count
    
    satisfactory_rating_percent = 80
    satisfactory_rating_count = (satisfactory_rating_percent / 100) * remaining_respondents
    
    needs_improvement_count = remaining_respondents - satisfactory_rating_count
    
    result = needs_improvement_count
    
    return result

print(solution())