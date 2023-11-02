def solution():
    """Five coworkers were talking during the lunch break. Roger, the oldest one, said that he has the same amount of experience in years as all four of the others combined and that his retirement should come when he accumulates 50 years of experience. Peter said that when he came to the company his daughter was 7 years old, and now she is 19 years old. Tom then said he has twice as many years of experience as Robert. Robert said that he has 4 years of experience less than Peter but 2 more years of experience than Mike. How many more years does Roger have to work before he retires?"""
    
    peter_daughter_age_diff = 12
    robert_peter_experience_diff = -4
    mike_robert_experience_diff = -2
    
    mike_experience = 8  # (Peter's experience - Robert's experience) + (Robert's experience - Mike's experience) = 4 + (-2) = 2, therefore Mike has 8 years of experience (Peter has 12 and Robert has 10)
    robert_experience = mike_experience + 2  # Robert has 2 more years of experience than Mike
    tom_experience = 2 * robert_experience  # Tom has twice as many years of experience as Robert
    peter_experience = robert_experience + peter_daughter_age_diff  # Peter has 4 years of experience less than Peter's current experience, which is the same as the age difference between his daughter when he started and now
    total_experience = peter_experience + mike_experience + robert_experience + tom_experience
    
    roger_experience = total_experience - peter_experience - mike_experience - robert_experience - tom_experience
    years_until_retirement = 50 - roger_experience
    
    return years_until_retirement

print(solution())