def solution():
    # Define Michael Jordan's birth year
    birth_year = 1963
    # Calculate the minimum age required to enter culinary apprenticeships
    minimum_age = 17
    # Determine if Michael Jordan meets the minimum age requirement
    if 2020 - birth_year >= minimum_age:
        # Check if Michael Jordan has a high school diploma or equivalent
        has_diploma = True # Assume Michael Jordan has a diploma
        if has_diploma:
            result = "yes"
        else:
            result = "no"
    else:
        result = "no"
    return result

print(solution())