def solution():
    """It’s February 2021. Mark was born in January 1976. Graham is 3 years younger than Mark, and Graham’s sister, Janice, is 1/2 the age of Graham. How old is Janice?"""
    # Calculate Mark's age as of February 2021
    mark_age = 2021 - 1976

    # Calculate Graham's age as of February 2021
    graham_age = mark_age - 3

    # Calculate Janice's age as of February 2021
    janice_age = graham_age / 2

    # Return the result
    result = janice_age
    return result

print(solution())