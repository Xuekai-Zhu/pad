def solution():
    
    jon_salary = 3000
    karen_salary = (4/3) * jon_salary
    karen_salary_3_months = karen_salary * 3
    months_to_match_salary = karen_salary_3_months / jon_salary
    result = months_to_match_salary
    return result

print(solution())