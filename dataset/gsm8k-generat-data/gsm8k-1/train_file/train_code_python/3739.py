def solution():
    """Grace's age is 3/8th the age of her grandmother. Her grandmother is twice the age of Grace's mother. If Grace's mother is 80 years old, how old is Grace?"""
    mother_age = 80
    grandmother_age = mother_age * 2
    grace_to_grandmother_ratio = 3 / 8
    grace_age = grandmother_age * grace_to_grandmother_ratio
    result = grace_age
    return result

print(solution())