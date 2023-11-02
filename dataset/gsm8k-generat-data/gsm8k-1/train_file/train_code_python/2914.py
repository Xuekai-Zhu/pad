def solution():
    """Adam and Tom are brothers. Adam is 8 years old and Tom is 12 years old. In how many years will their combined age be 44 years old?"""
    current_age_sum = 8 + 12
    target_age_sum = 44
    years_until_target_age_sum = (target_age_sum - current_age_sum)
    result = years_until_target_age_sum
    return result

print(solution())