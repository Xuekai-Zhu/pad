def solution():
    # Calculate Tom's current age
    Tom_current_age = 32 + 5  # Tom turned 32 years old 5 years ago
    Jim_7_years_ago = Tom_current_age / 2 + 5  # Jim was 5 years older than half Tom's age 7 years ago
    
    # Calculate Jim's current age
    Jim_current_age = Jim_7_years_ago + 7  # Jim's current age is 7 years more than his age 7 years ago
    
    # Calculate Jim's age in 2 years
    Jim_age_in_2_years = Jim_current_age + 2
    
    result = Jim_age_in_2_years
    return result

print(solution())