def solution():
    """In 5 years, Joey will be as old as Beth is now. If Joey is 9 now, how old was Joey when Beth was Joey's age now?"""
    # Define Joey's current age
    joey_age = 9

    # Calculate Beth's current age
    beth_age = joey_age + 5

    # Calculate the age difference between Joey and Beth
    age_difference = beth_age - joey_age

    # Calculate Joey's age when Beth was Joey's age now
    joey_age_at_that_time = joey_age - age_difference

    # Display Joey's age when Beth was Joey's age now
    result = joey_age_at_that_time
    return result

print(solution())