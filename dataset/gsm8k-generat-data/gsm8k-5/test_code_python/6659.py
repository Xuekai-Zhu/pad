def solution():
    sister_age = 2  # Maxwell's sister is currently 2 years old
    age_difference = 2  # Maxwell will always be 2 years older than his sister
    maxwell_age_in_2_years = 2 * (sister_age + age_difference)  # Maxwell's age in 2 years will be twice his sister's age
    maxwell_current_age = maxwell_age_in_2_years - 2  # Maxwell's current age is 2 years less than his age in 2 years

    result = maxwell_current_age
    return result

print(solution())