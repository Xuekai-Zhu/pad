def solution():
    """Kiarra is twice as old as Bea. Job is 3 times older than Bea. Figaro is 7 years older than Job. Harry is half as old as Figaro. If Kiarra is 30, how old is Harry?"""
    # Set up equations for each person's age
    # Kiarra = 30
    # Kiarra = 2*Bea
    # Job = 3*Bea
    # Figaro = Job + 7
    # Harry = 0.5*Figaro

    # Solve for Bea's age
    Bea = 30/2.0

    # Solve for Job's age
    Job = 3*Bea

    # Solve for Figaro's age
    Figaro = Job + 7

    # Solve for Harry's age
    Harry = 0.5*Figaro

    result = Harry
    return result

print(solution())