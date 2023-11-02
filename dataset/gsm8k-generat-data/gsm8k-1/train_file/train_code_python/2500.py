def solution():
    """Ann is 6 years old. Her brother Tom is now two times older. What will be the sum of their ages 10 years later?"""
    ann_age = 6
    tom_age = ann_age * 2
    ann_age_in_10yrs = ann_age + 10
    tom_age_in_10yrs = tom_age + 10
    sum_of_ages_in_10yrs = ann_age_in_10yrs + tom_age_in_10yrs
    result = sum_of_ages_in_10yrs
    return result

print(solution())