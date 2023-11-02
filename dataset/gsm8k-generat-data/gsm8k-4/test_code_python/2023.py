def solution():
    """If Beth is 18 years old and her little sister is 5, in how many years would she be twice her sister's age?"""
    # Define Beth's current age and her sister's current age
    beth_age = 18
    sister_age = 5

    # Initialize the year counter
    years = 0

    # While Beth's age is not twice her sister's age, increment the year counter and increase both ages by 1 year
    while beth_age != 2 * sister_age:
        years += 1
        beth_age += 1
        sister_age += 1

    # Return the result
    result = years
    return result

print(solution())