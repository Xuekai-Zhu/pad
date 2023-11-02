def solution():
    mike_earnings_multiplyer = 10
    salary_increase = 40
    fred_salary = 1000
    mike_salary = mike_earnings_multiplyer * fred_salary
    mike_salary_increase = mike_salary * (salary_increase / 100)
    mike_salary_now = mike_salary + mike_salary_increase
    result = mike_salary_now
    
    return result

print(solution())