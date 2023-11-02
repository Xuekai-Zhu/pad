def solution():
    """Mario's salary increased by 40% to $4000 this year. Bob's salary from last year was equal to three times Mario's salary this year. 
    If Bob's current salary is 20% more than his salary last year, what is his current salary?"""
    # Calculate Mario's salary from last year
    mario_salary_last_year = 4000 / 1.4

    # Calculate Bob's salary from last year
    bob_salary_last_year = 3 * mario_salary_last_year

    # Calculate Bob's current salary
    bob_salary_current = bob_salary_last_year * 1.2

    result = bob_salary_current
    return result

print(solution())