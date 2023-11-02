def solution():
    
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