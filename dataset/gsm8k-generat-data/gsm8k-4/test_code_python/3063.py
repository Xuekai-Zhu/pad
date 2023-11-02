def solution():
    """Five coworkers were talking during the lunch break. Roger, the oldest one, said that he has the same amount of experience in years as all four of the others combined and that his retirement should come when he accumulates 50 years of experience. Peter said that when he came to the company his daughter was 7 years old, and now she is 19 years old. Tom then said he has twice as many years of experience as Robert. Robert said that he has 4 years of experience less than Peter but 2 more years of experience than Mike. How many more years does Roger have to work before he retires?"""
    # Define the variables based on the given information
    robert_exp = peter_exp - 4
    mike_exp = robert_exp - 2
    tom_exp = 2 * robert_exp
    peter_daughter_age = 19
    peter_exp = peter_daughter_age - 7
    roger_exp = peter_exp + robert_exp + mike_exp + tom_exp
    
    # Calculate the remaining years until Roger retires
    years_left = 50 - roger_exp
    
    result = years_left
    return result

print(solution())