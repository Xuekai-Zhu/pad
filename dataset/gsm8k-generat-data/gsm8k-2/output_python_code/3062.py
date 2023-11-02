def solution():
    """Five coworkers were talking during the lunch break. Roger, the oldest one, said that he has the same amount of experience in years as all four of the others combined and that his retirement should come when he accumulates 50 years of experience. Peter said that when he came to the company his daughter was 7 years old, and now she is 19 years old. Tom then said he has twice as many years of experience as Robert. Robert said that he has 4 years of experience less than Peter but 2 more years of experience than Mike. How many more years does Roger have to work before he retires?"""
    # Let's start by defining Roger's experience as x
    x = 0

    # We know that Peter has been in the company for 12 years (19-7)
    # Therefore, Robert has 8 years of experience (12-4)
    # And Mike has 6 years of experience (8-2)
    mike_experience = 6
    robert_experience = 8

    # We know that Tom has twice as many years of experience as Robert
    tom_experience = 2 * robert_experience

    # Roger has the same amount of experience as all four of the others combined
    x = mike_experience + robert_experience + tom_experience + peter_experience

    # Roger's retirement will come when he accumulates 50 years of experience
    years_left = 50 - x

    result = years_left
    return result

print(solution())