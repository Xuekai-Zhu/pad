def solution():
    """Randolph is 5 years older than Sydney. Sydney is twice as old as Sherry. If Sherry is 25, how old is Randolph?"""
    # Define Sherry's age
    sherry_age = 25

    # Calculate Sydney's age
    sydney_age = sherry_age * 2

    # Calculate Randolph's age
    randolph_age = sydney_age + 5

    # return the result
    result = randolph_age
    return result

print(solution())