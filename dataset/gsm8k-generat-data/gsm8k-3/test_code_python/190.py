def solution():
    """Last year Dallas was 3 times the age of his sister Darcy. Darcy is twice as old as Dexter who is 8 right now. How old is Dallas now?"""
    # Define Dexter's age
    dexter_age = 8

    # Calculate Darcy's age
    darcy_age = 2 * dexter_age

    # Calculate Dallas' age last year
    dallas_last_year = 3 * darcy_age

    # Calculate Dallas' current age
    dallas_age = dallas_last_year + 1

    result = dallas_age
    return result

print(solution())