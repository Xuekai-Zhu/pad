def solution():
    """Djibo is 17 years old. Five years ago Djibo added his age with his sister's age and the sum was 35. How many years old is Djibo's sister today?"""
    djibo_age_now = 17
    sum_five_years_ago = 35
    sum_now = sum_five_years_ago + 2 * 5  # adding back the 5 years for each sibling
    djibo_plus_sister_now = sum_now
    djibo_plus_sister_five_years_ago = djibo_plus_sister_now - 2 * 5
    sister_age_now = djibo_plus_sister_now - djibo_age_now
    
    return sister_age_now

print(solution())