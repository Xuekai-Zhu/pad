def solution():
    claire_age_in_2_years = 20
    jessica_age_difference = 6

    # Calculate Claire's current age
    claire_current_age = claire_age_in_2_years - 2

    # Calculate Jessica's current age using the age difference between them
    jessica_current_age = claire_current_age + jessica_age_difference

    result = jessica_current_age
    return result

print(solution())