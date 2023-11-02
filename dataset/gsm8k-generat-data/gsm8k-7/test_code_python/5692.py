def solution():
    sebastian_age = 40
    sister_age = sebastian_age - 10
    years_ago = 5

    # Calculate the sum of Sebastian's and his sister's age 5 years ago
    sum_ages_5_years_ago = (sebastian_age - years_ago) + (sister_age - years_ago)

    # Calculate the father's age 5 years ago
    father_age_5_years_ago = sum_ages_5_years_ago / (3/4)

    # Calculate the father's current age
    father_age = father_age_5_years_ago + years_ago
    result = father_age
    return result

print(solution())