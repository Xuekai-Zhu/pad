def solution():
    """Viggo's age was 10 years more than twice his younger brother's age when his brother was 2. If his younger brother is currently 10 years old, what's the sum of their ages?"""
    younger_brother_age_when_Viggo_was_2 = 2
    current_younger_brother_age = 10
    difference_in_age = current_younger_brother_age - younger_brother_age_when_Viggo_was_2
    viggo_age_when_brother_was_2 = 2 * younger_brother_age_when_Viggo_was_2 + 10
    viggo_current_age = viggo_age_when_brother_was_2 + difference_in_age
    sum_of_ages = viggo_current_age + current_younger_brother_age
    result = sum_of_ages
    return result

print(solution())