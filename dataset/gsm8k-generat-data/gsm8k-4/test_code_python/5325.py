def solution():
    """After five years, Ron will be four times as old as Maurice. If Ron's age now is 43, how old is Maurice now?"""
    # Define Ron's current age and the age difference after 5 years
    ron_age = 43
    age_diff = 5

    # Calculate Maurice's age using the age difference ratio
    maurice_age = (ron_age - age_diff) / 3

    # return the result
    result = maurice_age
    return result

print(solution())