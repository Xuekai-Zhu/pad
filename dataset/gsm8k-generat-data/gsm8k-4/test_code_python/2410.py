def solution():
    """Freddy is 2 years younger than Stephanie. Stephanie is 4 times as old as Job. If Job is 5, how old is Freddy?"""
    # Define the age of Job
    job_age = 5

    # Calculate the age of Stephanie
    stephanie_age = job_age * 4

    # Calculate the age of Freddy
    freddy_age = stephanie_age - 2

    # return the result
    result = freddy_age
    return result

print(solution())