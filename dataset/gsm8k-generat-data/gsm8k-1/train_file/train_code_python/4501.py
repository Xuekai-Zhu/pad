def solution():
    """Arman is six times older than his sister. His sister is 2 years old four years ago. In how many years will Arman's age be 40?"""
    sister_age_now = 6  # Arman is 6 times older than his sister
    sister_age_four_years_ago = 2
    sister_age_now = sister_age_four_years_ago + 4  # add 4 years to get current age
    
    arman_age_now = sister_age_now * 6  # Arman is 6 times older than his sister
    
    years_until_arman_is_40 = 40 - arman_age_now
    
    result = years_until_arman_is_40
    
    return result

print(solution())