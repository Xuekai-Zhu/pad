def solution():
    """In 5 years, Joey will be as old as Beth is now. If Joey is 9 now, how old was Joey when Beth was Joey's age now?"""
    # Define Joey's current age and the age difference between him and Beth
    joey_age = 9
    age_difference = 5

    # Calculate Beth's current age
    beth_age = joey_age + age_difference

    # Calculate Joey's age when Beth was his current age
    joey_old_age = beth_age - age_difference

    result = joey_old_age
    return result

print(solution())