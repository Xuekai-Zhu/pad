def solution():
    # Calculate the age of Grace's grandmother
    mother_age = 80
    grandmother_age = 2 * mother_age / (3/8)

    # Calculate the age of Grace
    grace_age = grandmother_age * (3/8)
    result = grace_age
    return result

print(solution())