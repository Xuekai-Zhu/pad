def solution():
    kelsey_age_in_1999 = 25
    older_sister_age_diff = 3
    current_year = 2021

    # Calculate Kelsey's birth year
    kelsey_birth_year = current_year - kelsey_age_in_1999

    # Calculate the birth year of Kelsey's older sister
    older_sister_birth_year = kelsey_birth_year - older_sister_age_diff

    # Calculate the age of Kelsey's older sister
    older_sister_age = current_year - older_sister_birth_year
    result = older_sister_age
    return result

print(solution())