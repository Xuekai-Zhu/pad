def solution():
    # Define Ann's and Tom's current ages
    ann_age = 6
    tom_age = 2 * ann_age

    # Calculate their ages in 10 years
    ann_age_in_10_years = ann_age + 10
    tom_age_in_10_years = tom_age + 10

    # Calculate the sum of their ages in 10 years
    sum_of_ages_in_10_years = ann_age_in_10_years + tom_age_in_10_years

    result = sum_of_ages_in_10_years
    return result

print(solution())