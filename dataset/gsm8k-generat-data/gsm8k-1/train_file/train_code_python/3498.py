def solution():
    """Isabella is twice as old as Antonio. In 18 months, she will be 10 years old. How many months old is Antonio?"""
    isabella_age_in_months = 10 * 12 - 18
    isabella_age_in_years = isabella_age_in_months / 12
    antonio_age_in_years = isabella_age_in_years / 2
    antonio_age_in_months = antonio_age_in_years * 12
    result = antonio_age_in_months
    return result

print(solution())