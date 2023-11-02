def solution():
    """Freddy is 2 years younger than Stephanie. Stephanie is 4 times as old as Job. If Job is 5, how old is Freddy?"""
    # Define Job's age
    JOB_AGE = 5

    # Calculate Stephanie's age
    stephanie_age = JOB_AGE * 4

    # Calculate Freddy's age
    freddy_age = stephanie_age - 2

    # Display Freddy's age
    result = freddy_age
    return result

print(solution())