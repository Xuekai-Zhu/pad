def solution():
    ann_age = 6
    tom_age = 2 * ann_age

    # Calculate Ann's age 10 years from now
    ann_age_after_10_years = ann_age + 10

    # Calculate Tom's age 10 years from now
    tom_age_after_10_years = tom_age + 10

    # Calculate the sum of their ages 10 years from now
    sum_of_ages_after_10_years = ann_age_after_10_years + tom_age_after_10_years
    result = sum_of_ages_after_10_years
    return result

print(solution())