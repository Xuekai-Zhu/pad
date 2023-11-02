def solution():
    """Isabella is twice as old as Antonio. In 18 months, she will be 10 years old. How many months old is Antonio?"""
    isabella_age = 10 * 12 - 18
    antonio_age = isabella_age / 2
    antonio_months = antonio_age * 12
    result = antonio_months
    return result

print(solution())