def solution():
    """John is half times younger than his father, who is 4 years older than John's mother. If John's father is 40 years old, what's the age difference between John and his mother?"""
    # Calculate John's age
    john_age = 40 / 1.5

    # Calculate John's mother's age
    mother_age = 40 - 4 - john_age

    # Calculate the age difference between John and his mother
    age_difference = abs(john_age - mother_age)

    # return the result
    result = age_difference
    return result

print(solution())