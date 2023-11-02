def solution():
    # Calculate Djibo's age 5 years ago
    djibo_age_5_years_ago = 17 - 5

    # Calculate the sum of their ages 5 years ago
    sum_ages_5_years_ago = 35 - 2 * djibo_age_5_years_ago

    # Calculate Djibo's sister's age 5 years ago
    sister_age_5_years_ago = sum_ages_5_years_ago - djibo_age_5_years_ago

    # Calculate Djibo's sister's current age
    sister_age = sister_age_5_years_ago + 5
    result = sister_age
    return result

print(solution())