def solution():
    therese_age_diff = 2
    aivo_age_diff = 5
    leon_age_diff = 2

    # Calculate Aivo's age based on Therese's age difference
    aivo_age = 0 + aivo_age_diff

    # Calculate Therese's age based on Jolyn's age difference
    therese_age = aivo_age + therese_age_diff

    # Calculate Jolyn's age
    jolyn_age = therese_age + 2

    # Calculate Leon's age
    leon_age = aivo_age + leon_age_diff

    # Calculate the age difference between Jolyn and Leon
    age_diff = jolyn_age - leon_age
    result = age_diff
    return result

print(solution())