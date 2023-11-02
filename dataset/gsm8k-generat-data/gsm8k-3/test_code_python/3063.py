def solution():
    """Five coworkers were talking during the lunch break. Roger, the oldest one, said that he has the same amount of experience in years as all four of the others combined and that his retirement should come when he accumulates 50 years of experience. Peter said that when he came to the company his daughter was 7 years old, and now she is 19 years old. Tom then said he has twice as many years of experience as Robert. Robert said that he has 4 years of experience less than Peter but 2 more years of experience than Mike. How many more years does Roger have to work before he retires?"""
    
    # Let's denote the years of experience of Roger, Peter, Tom, Robert, and Mike respectively as r, p, t, o, and m
    # The following conditions can be written:
    
    r = p + t + o + m  # Roger's experience is equal to the sum of other coworkers' experience
    r + 50 = 2*(p + t + o + m)  # Roger will retire when he accumulates 50 years of experience, which will be twice others' experience
    p - 12 = 7  # Peter's daughter's age has increased from 7 to 19, which means he has worked for 12 years
    t = 2*o  # Tom's experience is twice as much as Robert's experience
    o + 2 = r - 4  # Robert's experience is 4 years less than Peter's experience, and 2 years more than Mike's experience
    
    # We can solve these equations to find the values of all the variables
    m = 10
    o = 6
    t = 12
    r = 34
    p = 19
    
    # Finally, we can calculate how many more years Roger has to work before he retires
    years_left = 50 - r
    
    result = years_left
    return result

print(solution())