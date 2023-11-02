def solution():
    current_age_jane = 28
    age_difference = 6  # Dara will be half the age of Jane in 6 years
    future_age_dara = (current_age_jane + age_difference) / 2  # Dara's age in 6 years
    age_required = 25  # The minimum age required to be employed at the company

    # Calculate the number of years it will take Dara to reach the minimum age required by the company
    years_to_reach_minimum_age = age_required - future_age_dara
    result = years_to_reach_minimum_age
    return result

print(solution())