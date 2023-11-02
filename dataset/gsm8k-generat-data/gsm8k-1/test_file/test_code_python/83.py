def solution():
    """A company pays each of its employees $600 in a month. The company has a policy of increasing the salaries of each of its employees by 10% of the initial salary every year for those who've stayed in the company for five years. If Sylvie just clocked 5 years in the company last December, what's her annual salary after three more years of service?"""
    initial_salary = 600 * 12
    years_of_service = 8
    years_since_promotion = years_of_service - 5
    percent_increase = years_since_promotion * 10
    salary_after_promotion = initial_salary + (initial_salary * (percent_increase / 100))
    result = salary_after_promotion / 12
    return result

print(solution())