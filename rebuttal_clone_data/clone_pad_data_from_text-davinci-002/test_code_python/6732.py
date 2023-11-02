def solution():
     initial_salary = 30000
     salary_increase = 2000
     years_of_increase = 4
     total_owed = (initial_salary * .3 + (initial_salary + salary_increase) * .3 + ((initial_salary + salary_increase) * 1.2) * .3 + ((initial_salary + salary_increase) * 1.2) * 1.2 * .3) - 1200
     result = total_owed
     return result

print(solution())