def solution():
    isabella_age_in_months = 10 * 12 - 18  # Isabella will be 10 years old in 18 months, convert to months
    isabella_age = isabella_age_in_months / 12  # Convert Isabella's age from months to years
    antonio_age = isabella_age / 2  # Isabella is twice as old as Antonio
    antonio_age_in_months = antonio_age * 12  # Convert Antonio's age from years to months
    result = antonio_age_in_months
    return result

print(solution())