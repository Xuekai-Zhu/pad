def solution():
    # Find Sebastian's sister's age
    sister_age = 40 - 10

    # Find the sum of their ages 5 years ago
    sum_ages_5_years_ago = (40 - 5) + (sister_age - 5)

    # Find the father's age 5 years ago
    father_age_5_years_ago = sum_ages_5_years_ago / (3/4)

    # Find the father's current age
    father_age = father_age_5_years_ago + 5*3

    result = father_age
    return result

print(solution())