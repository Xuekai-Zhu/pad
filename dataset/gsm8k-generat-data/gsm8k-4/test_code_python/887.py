def solution():
    """Kyle is 5 years older than Julian. Julian is 20 years younger than Frederick. Frederick is 2 times older than Tyson. If Tyson is 20, how old is Kyle?"""
    # Define Tyson's age
    tyson_age = 20

    # Calculate Frederick's age
    frederick_age = 2 * tyson_age

    # Calculate Julian's age
    julian_age = frederick_age - 20

    # Calculate Kyle's age
    kyle_age = julian_age + 5

    # return the result
    result = kyle_age
    return result

print(solution())