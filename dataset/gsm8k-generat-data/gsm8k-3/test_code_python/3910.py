def solution():
    """Mason is three times younger than Sydney and Sydney is six years younger than Mason's father. If Mason is 20 years old, how old is his father?"""
    # Define Mason's age
    mason_age = 20

    # Calculate Sydney's age
    sydney_age = 3 * mason_age

    # Calculate Mason's father's age
    father_age = sydney_age + 6

    # Display Mason's father's age
    result = father_age
    return result

print(solution())