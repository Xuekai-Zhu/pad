def solution():
    """Last year Dallas was 3 times the age of his sister Darcy. Darcy is twice as old as Dexter who is 8 right now. How old is Dallas now?"""
    # Define Dexter's age
    dexter_age = 8

    # Calculate Darcy's age
    darcy_age = dexter_age * 2

    # Calculate Dallas's age last year
    dallas_lastyear_age = darcy_age * 3

    # Calculate Dallas's current age
    dallas_age = dallas_lastyear_age + 1

    # Return the result
    result = dallas_age
    return result

print(solution())