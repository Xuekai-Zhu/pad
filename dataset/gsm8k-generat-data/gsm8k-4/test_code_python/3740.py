def solution():
    """Grace's age is 3/8th the age of her grandmother. Her grandmother is twice the age of Grace's mother. If Grace's mother is 80 years old, how old is Grace?"""
    # Define the age of Grace's mother
    mother_age = 80

    # Calculate the age of Grace's grandmother
    grandmother_age = mother_age * 2

    # Calculate the age of Grace
    grace_age = grandmother_age * (3/8)

    # return the result
    result = grace_age
    return result

print(solution())