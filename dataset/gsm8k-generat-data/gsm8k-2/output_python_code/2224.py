def solution():
    """Mario's salary increased by 40% to $4000 this year. Bob's salary from last year was equal to three times Mario's salary this year. If Bob's current salary is 20% more than his salary last year, what is his current salary?"""
    marios_salary = 4000
    bobs_salary_last_year = 3 * marios_salary
    bobs_salary_current = bobs_salary_last_year * 1.2
    result = bobs_salary_current
    return result

print(solution())