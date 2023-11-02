def solution():
    """Allen is 25 years younger than his mother. In 3 years, the sum of their ages will be 41. What is the present age of Allen's mother?"""
    sum_of_ages_in_3_years = 41
    age_difference = 25
    allen_age_in_3_years = (sum_of_ages_in_3_years - age_difference) / 2
    allen_current_age = allen_age_in_3_years - 3
    mother_current_age = allen_current_age + age_difference
    result = mother_current_age
    return result

print(solution())