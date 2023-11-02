def solution():
    """Kelsey turned 25 in 1999. Her older sister was born 3 years before Kelsey. It's currently 2021. How old is Kelsey's older sister?"""
    kelsey_age_in_1999 = 25
    older_sister_age_difference = 3
    older_sister_age_in_1999 = kelsey_age_in_1999 - older_sister_age_difference
    current_year = 2021
    age_difference_between_years = current_year - 1999
    older_sister_current_age = older_sister_age_in_1999 + age_difference_between_years
    result = older_sister_current_age
    return result

print(solution())