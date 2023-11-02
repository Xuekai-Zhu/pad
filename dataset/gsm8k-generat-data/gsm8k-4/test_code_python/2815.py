def solution():
    """In 10 years, Terry will be 4 times the age that Nora is currently. If Nora is currently 10 years old, how old is Terry now?"""
    # Define Nora's current age
    nora_age = 10

    # Calculate Terry's age in 10 years, based on the given condition
    terry_age_in_10_years = nora_age * 4

    # Calculate Terry's current age
    terry_age = terry_age_in_10_years - 10

    # return the result
    result = terry_age
    return result

print(solution())