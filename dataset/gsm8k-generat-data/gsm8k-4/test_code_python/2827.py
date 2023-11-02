def solution():
    """In five years, Grant will be 2/3 the age of the hospital that he is hired into. If Grant is currently 25 years old, how old is the hospital now?"""
    # Define Grant's current age and the number of years in the future
    grant_age = 25
    future_years = 5

    # Calculate Grant's age in the future
    grant_future_age = grant_age + future_years

    # Calculate the hospital's age in the future
    hospital_future_age = (3/2) * grant_future_age

    # Subtract the number of future years to get the current age of the hospital
    hospital_age = hospital_future_age - future_years

    # Return the result
    result = hospital_age
    return result

print(solution())