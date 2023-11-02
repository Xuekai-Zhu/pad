def solution():
    
    sister_age_now = 6  
    sister_age_four_years_ago = 2
    sister_age_now = sister_age_four_years_ago + 4  
    
    arman_age_now = sister_age_now * 6  
    
    years_until_arman_is_40 = 40 - arman_age_now
    
    result = years_until_arman_is_40
    
    return result

print(solution())