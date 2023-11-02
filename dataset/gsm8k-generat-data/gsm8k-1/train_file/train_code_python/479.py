def solution():
    """Kirt has a $6000 monthly salary when he started his job. After a year of working, his salary increased by 30%. How much are his total earnings after 3 years?"""
    initial_salary = 6000
    salary_increase = 30/100
    salary_after_one_year = initial_salary + (initial_salary * salary_increase)
    salary_after_two_years = salary_after_one_year + (salary_after_one_year * salary_increase)
    salary_after_three_years = salary_after_two_years + (salary_after_two_years * salary_increase)
    total_earnings = initial_salary*12 + salary_after_one_year*12 + salary_after_two_years*12 + salary_after_three_years*12
    result = total_earnings
    return result

print(solution())