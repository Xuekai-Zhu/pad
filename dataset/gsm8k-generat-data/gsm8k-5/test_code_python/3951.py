def solution():
    kelsey_age_in_1999 = 25  # Kelsey turned 25 in 1999
    sister_age_difference = 3  # Kelsey's older sister was born 3 years before her
    current_year = 2021  # It's currently 2021

    # Calculate Kelsey's age in 2021
    kelsey_age_in_2021 = current_year - 1999 + kelsey_age_in_1999

    # Calculate Kelsey's older sister's age in 2021
    sister_age_in_2021 = kelsey_age_in_2021 + sister_age_difference
    result = sister_age_in_2021
    return result

print(solution())