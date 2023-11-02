def solution():
    """Djibo is 17 years old. Five years ago Djibo added his age with his sister's age and the sum was 35. How many years old is Djibo's sister today?"""
    djibo_age = 17
    five_years_ago_sum = 35
    sum_now = five_years_ago_sum + 2 * 5  # adding 2 times 5 years ago since it includes both Djibo and his sister
    sister_age_now = sum_now - djibo_age
    result = sister_age_now
    return result

print(solution())