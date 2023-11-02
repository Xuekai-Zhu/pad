def solution():
    """Grace's age is 3/8th the age of her grandmother. Her grandmother is twice the age of Grace's mother. If Grace's mother is 80 years old, how old is Grace?"""
    mother_age = 80
    grandmother_age = 2 * mother_age
    grace_age = (3/8) * grandmother_age
    result = grace_age
    return result

print(solution())