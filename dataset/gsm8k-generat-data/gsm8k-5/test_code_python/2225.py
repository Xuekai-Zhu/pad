def solution():
    mario_salary_this_year = 4000  # Mario's salary this year is $4000
    mario_salary_last_year = mario_salary_this_year / 1.4  # Mario's salary increased by 40% this year

    # Bob's salary from last year was equal to three times Mario's salary this year
    bob_salary_last_year = 3 * mario_salary_this_year

    # Bob's current salary is 20% more than his salary last year
    bob_salary_this_year = bob_salary_last_year * 1.2

    result = bob_salary_this_year
    return result

print(solution())