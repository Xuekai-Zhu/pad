def solution():
    """Grace's age is 3/8th the age of her grandmother. Her grandmother is twice the age of Grace's mother. If Grace's mother is 80 years old, how old is Grace?"""
    # Define Grace's mother's age and calculate her grandmother's age
    mother_age = 80
    grandmother_age = mother_age * 2

    # Calculate Grace's age
    grace_age = grandmother_age * (3/8)

    # Display Grace's age
    result = grace_age
    return result

print(solution())