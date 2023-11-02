def solution():
    Mario_salary_this_year = 4000
    Mario_salary_last_year = Mario_salary_this_year / 1.4
    Bob_salary_last_year = 3 * Mario_salary_last_year
    Bob_salary_this_year = Bob_salary_last_year * 1.2
    
    result = Bob_salary_this_year
    
    return result

print(solution())