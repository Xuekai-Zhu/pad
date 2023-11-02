def solution():
    starting_salary = 6000
    salary_increase = 0.3
    salary_after_one_year = starting_salary + (starting_salary * salary_increase)
    total_earnings = starting_salary + salary_after_one_year # Year 1 
    total_earnings += (salary_after_one_year * (1 + salary_increase)) # Year 2 
    total_earnings += (salary_after_one_year * (1 + salary_increase)) # Year 3
    result = total_earnings * 3
    return result

print(solution())